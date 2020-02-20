#Se importan las librerías requeridas por el BOT:
import mod_fixture as fix
import resultados as res
import os
import shutil
from fotosRes import Root
import PTC
import funciones as fd
from fotosTabla import Root2
from fotoCampeon import Root3
import time
import facebook
import pickle
import datetime

#Se calcula la fecha y hora actual.
ahora=datetime.datetime.now()
print("Hora: "+str(ahora.hour)+":"+str(ahora.minute)+"."+str(ahora.second))
ahora = datetime.datetime.now()
maniana = ahora+datetime.timedelta(days=0) #Si se desea que sea al día siguiente: days=1, si se desea que sea en el mismo día days=0. Esto para cuando se retoma la simulación pasada la medianoche.

#PROGRAMAMOS AL BOT PARA QUE EJECUTE AL DÍA SIGUIENTE A LAS 10AM:
maniana_10am = datetime.datetime(maniana.year,maniana.month,maniana.day,10,00,00)
print((maniana_10am-ahora).total_seconds())
time.sleep((maniana_10am-ahora).total_seconds())

v_45min = 2697 #2700
v_30min = 1800 #1800
v_16horas = 60300 #57600

v_entre_p = 2697 #600
v_fin_fecha = 1800 #600

v_2dasim_maniana=60300

# Flag que indica si el BOT publicará en Facebook o no.
# 1: Publica, 0: Genera los resultados localmente (para debuggeo y mejoras)
flg_post = 1

# Flag que indica si el BOT está retomando una simulación anterior o empieza de 0.
# 1: Se retoma la simulación anterior. 0: Se genera una simulación nueva.
flg_retomar_sim = 1

#Token de acceso a la página de Facebook.
token ='EAACVS6jUj0QBAMLK0UnT2lbrwrOZAeiWnsBej2vPYZBvxB8OTYpkpV9R5dkpS6gPuBjaRmcqcZCf5U6kX3bjxg6fQVSeOeWdqdYWL0bguCwCUYWNpkyHBKh3pcyGiSsAznzwJiIQJftiWmvf6QGhZBRaF51RbW3OltlIZBIN0rgZDZD'
fb=facebook.GraphAPI(access_token= token)

#Ubicación de los backups en la memoria para escribir y leer las variables útiles
pickle_backups_fixture='D:\Google Drive\Daniel M\Codigos\Codigos míos\Facebook\Peruvian Football Bot\Backups\pback_ups_fixture.pkl' #Información de los fixtures
pickle_backups_fecha='D:\Google Drive\Daniel M\Codigos\Codigos míos\Facebook\Peruvian Football Bot\Backups\pback_ups_fecha.pkl' #Información de las fechas
pickle_backups_partido='D:\Google Drive\Daniel M\Codigos\Codigos míos\Facebook\Peruvian Football Bot\Backups\pback_ups_partido.pkl' #Información de los partidos
pickle_backups_equipos='D:\Google Drive\Daniel M\Codigos\Codigos míos\Facebook\Peruvian Football Bot\Backups\pback_ups_equipos.pkl' #Información de los equipos

#Si vamos a iniciar una nueva simulación, es importante borrar los backups, para evitar problemas en el futuro:
if flg_retomar_sim==0:
    try:
        os.remove(pickle_backups_fixture)
    except FileNotFoundError:
        pass
    try:
        os.remove(pickle_backups_fecha)
    except FileNotFoundError:
        pass
    try:
        os.remove(pickle_backups_partido)
    except FileNotFoundError:
        pass
    try:
        os.remove(pickle_backups_equipos)
    except FileNotFoundError:
        pass



tiempo_perdido = 0
intentar_publicar = 0

t_entre_final_y_c = 0  # 299

#Obtengo la ubicación actual del folder:
current_folder = os.getcwd()
#import plantillas as plant


#Equipos en disputa de la Liga:
Equipos_dict={1:'Alianza Lima',
              2: 'Sporting Cristal',
              3:'Universitario',
              4:'Sport Boys',
              5: 'Cantolao',
              6: 'Alianza UDH',
              7: 'Atletico Grau',
              8: 'Ayacucho FC',
              9: 'Mannucci',
              10: 'Carlos Stein',
              11: 'Cienciano',
              12: 'Real Garcilaso',
              13: 'Binacional',
              14: 'Llacuabamba',
              15: 'Municipal',
              16: 'FBC Melgar',
              17: 'Sport Huancayo',
              18: 'U Cesar Vallejo',
              19: 'U San Martin',
              20: 'UTC'}

#Si se está retomando una simulación, recuperaremos desde la memoria las estadísticas de cada equipo.
if flg_retomar_sim==1:
    r_pickle_backups_equipos=open(pickle_backups_equipos, 'rb')
    Equipo = pickle.load(r_pickle_backups_equipos)
    r_pickle_backups_equipos.close()
#Caso contrario, inicializaremos dichas estadísticas:
else:
    Equipo = [PTC.Equipo(Equipos_dict[i+1]) for i in range(len(Equipos_dict))]
    #Y se guardan
    w_pickle_backups_equipos=open(pickle_backups_equipos, 'wb')
    pickle.dump(Equipo, w_pickle_backups_equipos)
    w_pickle_backups_equipos.close()


if flg_retomar_sim==1:
    #Si se está retomando una simulación anterior, se deberá empezar desde la fecha hasta la cual la simulación había llegado de manera satisfactoria:
    try:
        #Se intenta leer la última fecha  en la que quedó la simulación:
        r_pickle_backups_fecha = open(pickle_backups_fecha, 'rb')
        inicio_fecha = pickle.load(r_pickle_backups_fecha)
        r_pickle_backups_fecha.close()
    except FileNotFoundError:
        #Pero puede que nunca se haya escrito... por lo que la fecha era la fecha 1:
        inicio_fecha=0
    except EOFError:
        #Por si no se llegó a borrar, pero estaba vacía:
        inicio_fecha = 0

    #Además, evidentemente, con el Fixture TAL CUAL estaba previsto anteriormente:
    r_pickle_backups_fixture=open(pickle_backups_fixture,'rb')
    Fixture_numeros, Fixture = pickle.load(r_pickle_backups_fixture)
    r_pickle_backups_fixture.close()
else:
    #Si se está simulando DESDE 0, la simulación deberá empezar por la fecha 1, por lo que inicio_fecha debe tener el valor de 0 (fecha-1):
    inicio_fecha = 0
    #Además, el fixture deberá ser generado aleatoriamente:
    Fixture_numeros = fix.make_schedule(len(Equipos_dict))
    Fixture = fix.crear_fixture(Equipos_dict,Fixture_numeros)
    #A fin de poder retomar una simulación (de suceder algún imprevisto), se guarda el fixture en la memoria:
    w_pickle_backups_fixture = open(pickle_backups_fixture, 'wb')
    pickle.dump([Fixture_numeros, Fixture], w_pickle_backups_fixture)
    w_pickle_backups_fixture.close()

#m: fecha
#n: partido
#k: equipo (local 0, visita 1)
#Fixture[m][n][0] es el nombre del equipo local y  Fixture[m][n][1] es el nombre del equipo visita

#Este for corre fecha a fecha:
for m_for in range(inicio_fecha, len(Fixture_numeros)):
    print(m_for)
    #Si el bot ejecutó la fecha correctamente, la variable inicio_fecha tomará el valor de m_for
    w_pickle_backups_fecha=open(pickle_backups_fecha, 'wb')
    pickle.dump(m_for, w_pickle_backups_fecha)
    w_pickle_backups_fecha.close()

    if m_for == inicio_fecha and flg_retomar_sim:
        print("Se resuelve desde aquí debido a errores anteriores")
        t_entre_partidos = v_entre_p
        t_entre_f_y_t = v_fin_fecha
    else:
        t_entre_partidos = v_45min  # 2699
        t_entre_f_y_t = v_30min  # 1799
    m = m_for + 1
    print('\n\n\n\nfecha: ' + str(m))

    #Se crea la carpeta de la fecha con los backups de la fecha. xd.
    try:
        os.mkdir(current_folder + "\Backups\Fecha_" + str(m))
        # print("\n \nSe creó la carpeta con total y rotundo éxito. SABPEEE")
    except OSError:
        pass

    #Se guarda la info de la fecha TAMBIÉN en una carpeta aparte (de modo que tengamos backups de todas las fechas uwu):
    w_pickle_backups_fecha=open(current_folder + "\Backups\Fecha_" + str(m)+"\pback_ups_fecha.pkl", 'wb')
    pickle.dump(m_for, w_pickle_backups_fecha)
    w_pickle_backups_fecha.close()

    if m_for == inicio_fecha and flg_retomar_sim == 1:
        pass
    else:
        try:
            #Se borran los resultados (fotos) de la fecha (de simulaciones anteriores). Solo es para evitar que las carpetas se llenen de imágenes que no se usarán.
            #NOTA: Este paso solo debe hacerse cuando no se está retomando una simulación anterior.
            shutil.rmtree(current_folder + "\Resultados\Fotos_Fecha" + str(m))
        except OSError:
            pass

    try:
        os.mkdir(current_folder + "\Resultados\Fotos_Fecha" + str(m))
        # print("\n \nSe creó la carpeta con total y rotundo éxito. SABPEEE")
    except OSError:
        pass
        # print("\n \nNo pudo crearse la carpeta... quizas ya existía?")
    else:
        pass
        # print("\n \nLa carpeta ya había sido creada")

    if m_for == inicio_fecha and flg_retomar_sim == 1:
        # Si se está retomando una simulación anterior, se deberá empezar desde el partido hasta el cual la simulación había llegado de manera satisfactoria:
        r_pickle_backups_partido=open(pickle_backups_partido,'rb')
        inicio_partido = pickle.load(r_pickle_backups_partido)
        r_pickle_backups_partido.close()
    else:
        # Si se está simulando DESDE 0, la simulación deberá empezar por la fecha 1, por lo que inicio_fecha debe tener el valor de 0 (fecha-1):
        inicio_partido = [0]

    #Este for corre partido por partido de una fecha en particular
    for n_for in range(inicio_partido[0], int(len(Equipos_dict)/2)):
        n=n_for
        orden_local = fd.getKeysByValue(Equipos_dict,Fixture[m_for][n][0])[0]-1
        orden_visita = fd.getKeysByValue(Equipos_dict,Fixture[m_for][n][1])[0]-1
        t_ult_resLoc=Equipo[orden_local].ult_res
        t_ult_resVis = Equipo[orden_visita].ult_res
        t_gfavorLoc = Equipo[orden_local].gfavor
        t_gfavorVis = Equipo[orden_visita].gfavor

        (scoreLocal,scoreVisita,resultado)=res.Score(1.98,1.2,Fixture[m_for][n][0],Fixture[m_for][n][1],t_ult_resLoc,t_ult_resVis, t_gfavorLoc, t_gfavorVis)
        (pos_cambiosLocal,t_cambiosLocal)=res.cambios(0.85,0.1,0.3)
        (pos_cambiosVisita,t_cambiosVisita)=res.cambios(0.85,0.1,0.3)


        Equipo[orden_local].marcador(scoreLocal,scoreVisita)
        Equipo[orden_visita].marcador(scoreVisita, scoreLocal)
        if scoreLocal>scoreVisita:
            Equipo[orden_local].victoria()
            Equipo[orden_visita].derrota()
        elif scoreLocal==scoreVisita:
            Equipo[orden_local].empate()
            Equipo[orden_visita].empate()
        else:
            Equipo[orden_visita].victoria()
            Equipo[orden_local].derrota()
        Equipo[orden_local].f_dif_goles(scoreLocal,scoreVisita)
        Equipo[orden_visita].f_dif_goles(scoreVisita, scoreLocal)

        plantillaLocal=res.TPlantillas(Fixture[m_for][n][0], t_cambiosLocal, pos_cambiosLocal)
        plantillaVisita=res.TPlantillas(Fixture[m_for][n][1], t_cambiosVisita, pos_cambiosVisita)
        jGolesLocal=res.j_Goles(scoreLocal, 0.4,0.1)
        jGolesVisita=res.j_Goles(scoreVisita, 0.4,0.1)
        jGolesLocal_nombres=[]
        jGolesVisita_nombres=[]
        t_golesLocal=res.T_Goles(scoreLocal)
        t_golesVisita=res.T_Goles(scoreVisita)
        (rojasLocal,rojasVisita, amarillasLocal,amarillasVisita, canc_partido)= res.nTarjetas(0.15,0.4)
        if rojasLocal >11:
            rojasLocal=11
        if rojasVisita>11:
            rojasVisita=11

        #Los tiempos de las tarjetas se ven como una lista de 2 listas.
        #La primera lista corresponde al minuto en el que fueron puestas las tarjetas
        #durante el primer tiempo. La segunda lista corresponde a lo mismo, pero en el
        #segundo tiempo
        (t_rojasLocal,t_amarillasLocal)=res.TiemposTarjetas(rojasLocal, amarillasLocal)
        (t_rojasVisita,t_amarillasVisita)=res.TiemposTarjetas(rojasVisita, amarillasVisita)
        (jAmarillasLocal,jRojasLocal)=res.jTarjetas(rojasLocal, amarillasLocal)
        (jAmarillasVisita,jRojasVisita)=res.jTarjetas(rojasVisita, amarillasVisita)


        ##Se asignan los jugadores que metieron goles:
        jGolesLocal_nombres=res.AsignarJugGoles(jGolesLocal, t_golesLocal, pos_cambiosLocal, t_cambiosLocal, plantillaLocal)
        jGolesVisita_nombres=res.AsignarJugGoles(jGolesVisita, t_golesVisita, pos_cambiosVisita, t_cambiosVisita, plantillaVisita)


        #Se asignan los jugadores que recibieron tarjetas para el Local:
        jAmarillasLocal_nombres=res.AsignarJugTarjetas(jAmarillasLocal, t_amarillasLocal, pos_cambiosLocal, t_cambiosLocal, plantillaLocal)
        jRojasLocal_nombres=res.AsignarJugTarjetas(jRojasLocal, t_rojasLocal, pos_cambiosLocal, t_cambiosLocal, plantillaLocal)
        #Nos aseguramos que los que tengan doble amarilla tengan roja:
        (jRojasLocal_nombres,t_rojasLocal)=res.DobleAmarilla_Roja(jAmarillasLocal_nombres, jRojasLocal_nombres,t_rojasLocal,t_amarillasLocal)


        #Se asignan los jugadores que recibieron tarjetas para la Visita:
        jAmarillasVisita_nombres=res.AsignarJugTarjetas(jAmarillasVisita, t_amarillasVisita, pos_cambiosVisita, t_cambiosVisita, plantillaVisita)
        jRojasVisita_nombres=res.AsignarJugTarjetas(jRojasVisita, t_rojasVisita, pos_cambiosVisita, t_cambiosVisita, plantillaVisita)
        #Nos aseguramos que los que tengan doble amarilla tengan roja:
        (jRojasVisita_nombres,t_rojasVisita)=res.DobleAmarilla_Roja(jAmarillasVisita_nombres, jRojasVisita_nombres,t_rojasVisita,t_amarillasVisita)

        resultado_final=res.TablaResultado(scoreLocal, scoreVisita, Fixture[m_for][n][0],Fixture[m_for][n][1],jGolesLocal_nombres, jGolesVisita_nombres, t_golesLocal, t_golesVisita, resultado, pos_cambiosLocal, t_cambiosLocal,pos_cambiosVisita,t_cambiosVisita, t_rojasLocal,t_amarillasLocal, t_rojasVisita,t_amarillasVisita, jAmarillasLocal_nombres, jRojasLocal_nombres,jAmarillasVisita_nombres,jRojasVisita_nombres)
        # Creamos el folder con las fotos de resultados de la fecha actual:

        root = Root()
        root.creatCanvasImage(Fixture[m_for][n][0],Fixture[m_for][n][1],scoreLocal,scoreVisita,m, jGolesLocal_nombres, t_golesLocal, jGolesVisita_nombres, t_golesVisita)

        print('\n'+resultado_final)
        img_path=current_folder+'\Resultados\Fotos_Fecha'+str(m)+'\A_ '+str(Fixture[m_for][n][0])+' vs '+str(Fixture[m_for][n][1])+'.png'
        if flg_post==1:
            intentar_publicar = 0
            while intentar_publicar != 1:
                try:
                    fb.put_photo(image=open(img_path, 'rb'), message="¡Final del partido!\n"+resultado_final+"\n#PorLosMemesDeNuestroFutbol")
                    intentar_publicar = 1
                    print("Se publicó en Facebook con éxito")
                except Exception as e:
                    tiempo_perdido += 60
                    print("Error de conexión, volviendo a probar en 60 segundos")
                    print("Tiempo perdido: " + str(tiempo_perdido) + " segundos.")
                    time.sleep(60)
                    intentar_publicar = 0
        #Si el partido terminó correctamente, la variable inicio_partido tomará el valor de n_for:
        w_pickle_backups_partido=open(pickle_backups_partido, 'wb')
        pickle.dump([n_for+1], w_pickle_backups_partido)
        w_pickle_backups_partido.close()

        #También se guarda en la carpeta nueva:
        w_pickle_backups_partido = open(current_folder + "\Backups\Fecha_" + str(m)+"\pback_ups_partido.pkl", 'wb')
        pickle.dump([n_for + 1], w_pickle_backups_partido)
        w_pickle_backups_partido.close()

        # Se sobreescriben las nuevas estadísticas de los equipos:
        w_pickle_backups_equipos = open(pickle_backups_equipos, 'wb')
        pickle.dump(Equipo, w_pickle_backups_equipos)
        w_pickle_backups_equipos.close()

        w_pickle_backups_equipos = open(current_folder + "\Backups\Fecha_" + str(m)+"\pback_ups_equipos.pkl", 'wb')
        pickle.dump(Equipo, w_pickle_backups_equipos)
        w_pickle_backups_equipos.close()

        print("Terminó el partido número " + str(n_for + 1))
        #Pongo el bot a descansar entre cada partido:
        if n_for+1<int(len(Equipos_dict)/2):
            print("entro entre partidos")
            mas_45min=maniana_10am+datetime.timedelta(minutes=45*(n_for+1))
            hora_mas45min=datetime.datetime(mas_45min.year,mas_45min.month,mas_45min.day,mas_45min.hour, mas_45min.minute, 00)
            ahora = datetime.datetime.now()
            print("Hora: " + str(ahora.hour) + ":" + str(ahora.minute))
            #time.sleep(t_entre_partidos)
            print((hora_mas45min-ahora).total_seconds())
            time.sleep((hora_mas45min-ahora).total_seconds())

    if inicio_partido[0]==int(len(Equipos_dict)/2) and flg_retomar_sim:
        pass
    else:
        Tabla_Posiciones = sorted(Equipo, key=lambda x: x.gfavor, reverse=True)
        Tabla_Posiciones = sorted(Tabla_Posiciones, key=lambda x: x.dif_goles, reverse=True)
        Tabla_Posiciones = sorted(Tabla_Posiciones, key=lambda x: x.puntaje, reverse=True)

        root2 = Root2()
        root2.creatCanvasImage(Tabla_Posiciones, m)
        img_path = current_folder + '\Resultados\Fotos_Fecha' + str(m) + '\A_Tabla_Posiciones.png'

        ahora = datetime.datetime.now()
        print("Hora: " + str(ahora.hour) + ":" + str(ahora.minute))
        time.sleep(t_entre_f_y_t)
        if flg_post == 1:
            intentar_publicar = 0
            while intentar_publicar != 1:
                try:
                    fb.put_photo(image=open(img_path, 'rb'), message="¡Terminó la fecha "+ str(m)+" del Bot 1 Rovistar!\nMira la tabla de posiciones actualizada aquí:\n#PorLosMemesDeNuestroFutbol")
                    intentar_publicar=1
                    print("Se publicó en Facebook con éxito")
                except Exception:
                    tiempo_perdido+=60
                    print("Error de conexión, volviendo a probar en 60 segundos")
                    print("Tiempo perdido: "+str(tiempo_perdido)+" segundos.")
                    time.sleep(60)
                    intentar_publicar=0

        #Pongo a descansar al Bot entre fechas:
        if m_for == inicio_fecha and flg_retomar_sim:
            print("Se resuelve desde aquí debido a errores anteriores")
            t_entre_fechas = v_2dasim_maniana
        else:
            t_entre_fechas = v_16horas - tiempo_perdido  # 57599
        tiempo_perdido=0
        if m < len(Fixture_numeros):
            print("entro entre fechas")
            ahora = datetime.datetime.now()
            print("Hora: " + str(ahora.hour) + ":" + str(ahora.minute))
            ahora = datetime.datetime.now()
            maniana = ahora + datetime.timedelta(days=1)
            # PROGRAMAMOS AL BOT PARA QUE EJECUTE MAÑANA A LAS 10AM:
            maniana_10am = datetime.datetime(maniana.year, maniana.month, maniana.day, 10, 00, 00)
            print("El bot descansará por "+ str((maniana_10am - ahora).total_seconds())+" segundos")
            time.sleep((maniana_10am - ahora).total_seconds())
            #time.sleep(t_entre_fechas)



try:
    os.mkdir(current_folder + "\Resultados\Fotos_Final")
    # print("\n \nSe creó la carpeta con total y rotundo éxito. SABPEEE")
except OSError:
    pass
    # print("\n \nNo pudo crearse la carpeta... quizás ya existía?")
else:
    pass

root3 = Root3()
root3.creatCanvasImage(Tabla_Posiciones[0].nom_dict)

img_path = current_folder + '\Resultados\Fotos_Final\Resultado_Campeon.png'
if flg_post == 1:
    time.sleep(t_entre_final_y_c)
    ahora = datetime.datetime.now()
    print("Hora: " + str(ahora.hour) + ":" + str(ahora.minute))
    intentar_publicar = 0
    while intentar_publicar != 1:
        try:
            fb.put_photo(image=open(img_path, 'rb'), message="¡Felicidades, "+Tabla_Posiciones[0].nom_dict+", campeón del Bot 1 Rovistar 2020!\n#PorLosMemesDeNuestroFutbol")
            intentar_publicar = 1
            print("Se publicó en Facebook con éxito")
        except Exception:
            tiempo_perdido += 60
            print("Error de conexión, volviendo a probar en 60 segundos")
            print("Tiempo perdido: "+str(tiempo_perdido)+" segundos.")
            time.sleep(60)
            intentar_publicar = 0



