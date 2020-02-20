import random as rd
import plantillas as plant

prob_penal=0.1

def Score(prom_goles, desv_std, e_local, e_visita, ult_resLoc,ult_resVis, gfavorLoc, gfavorVis):
    golesPartido=round(rd.gauss(prom_goles, desv_std))
    if golesPartido<0:
        golesPartido=0
    golesLocal=rd.randint(0,golesPartido)
    golesVisita=golesPartido-golesLocal

    if rd.random()<0.05:
        golesLocal+=2
    elif rd.random()<0.15:
        golesLocal+=1
    else:
        golesLocal=golesLocal

    #Si el equipo local ganó su último partido, tiene más chances de meter goles extra:
    if ult_resLoc==1:
        if rd.random()<0.05:
            golesLocal+=2
        elif rd.random()<0.15:
            golesLocal+=1
        else:
            golesLocal=golesLocal
    # Si perdió, menos goles:
    if ult_resLoc==-1:
        if rd.random()<0.05:
            golesLocal-=2
        elif rd.random()<0.15:
            golesLocal-=1
        else:
            golesLocal=golesLocal
        if golesLocal<0:
            golesLocal=0

    #Los equipos tienen gfavorLoc/100 probabilidades de meter goles extra:
    if rd.random()< gfavorLoc/200:
        golesLocal+=2
    elif rd.random()< gfavorLoc/100:
        golesLocal+=1
    else:
        pass

    # Si el equipo visita ganó su último partido, tiene más chances de meter goles extra:
    if ult_resVis==1:
        if rd.random()<0.05:
            golesVisita+=2
        elif rd.random()<0.15:
            golesVisita+=1
        else:
            golesVisita=golesVisita
    #Si perdió, menos goles:
    if ult_resVis==-1:
        if rd.random()<0.05:
            golesVisita-=2
        elif rd.random()<0.15:
            golesVisita-=1
        else:
            golesVisita=golesVisita
        if golesVisita<0:
            golesVisita=0

    #Los equipos tienen gfavorLoc/100 probabilidades de meter goles extra:
    if rd.random()< gfavorVis/200:
        golesVisita+=2
    elif rd.random()< gfavorVis/100:
        golesVisita+=1
    else:
        pass

    return (golesLocal, golesVisita, e_local+" "+str(golesLocal)+" - "+str(golesVisita)+" "+e_visita)

def T_Goles(n_goles):
    n_goles_1T=rd.randint(0,n_goles)
    n_goles_2T=n_goles-n_goles_1T
    cont=0
    t_goles_1T=[]
    t_goles_2T=[]
    while(cont<n_goles_1T):
        cont+=1
        t_goles_1T.append(rd.randint(0,45))
    t_goles_1T.sort()
    for ii in range(len(t_goles_1T)):
        if ii>0:
            if t_goles_1T[ii]==t_goles_1T[ii-1]:
                for jj in range(ii,len(t_goles_1T)):
                    t_goles_1T[jj]+=1 
    cont=0
    while(cont<n_goles_2T):
        cont+=1
        t_goles_2T.append(rd.randint(0,45))
    t_goles_2T.sort()
    for ii in range(len(t_goles_2T)):
        if ii>0:
            if t_goles_2T[ii]==t_goles_2T[ii-1]:
                for jj in range(ii,len(t_goles_2T)):
                    t_goles_2T[jj]+=1         
      
    t_goles=[t_goles_1T,t_goles_2T]
    return t_goles

#Para un equipo en específico. La probDelantero te da la probabilidad de que sea un
#delantero el que meta el gol. Probaré con un 40%.
def j_Goles(n_goles, probDelantero, probArquero):
    jGoles=[]
    for i in range(n_goles):
        if rd.random()<probDelantero:
            jGoles.append(rd.randint(10,11))
        elif rd.random()<probArquero+probDelantero:
            jGoles.append(rd.randint(1,11))
        else:
            jGoles.append(rd.randint(2, 11))
    return jGoles



#Esto es para ambos equipos:
def nTarjetas(prob_rojas,prob_amarillas):
    n_rojas=0
    if rd.random()<prob_rojas:
        n_rojas+=1
        while(rd.random()<prob_rojas):
            n_rojas+=1
            if n_rojas>=22:
                break
    n_amarillas=0
    if rd.random()<prob_amarillas:
        n_amarillas+=1
        while(rd.random()<prob_amarillas):
            n_amarillas+=1
            if n_amarillas>=22:
                break
    n_rojasLocal=rd.randint(0,n_rojas)
    n_rojasVisita=n_rojas-n_rojasLocal
    n_amarillasLocal=rd.randint(0,n_amarillas)
    n_amarillasVisita=n_amarillas-n_amarillasLocal
    if n_rojasLocal>=5:
        partido_cancelado=1
        n_rojasLocal=5
    elif n_rojasVisita>=5:
        partido_cancelado=1
        n_rojasVisita=5
    else:
        partido_cancelado=0
    return (n_rojasLocal,n_rojasVisita,n_amarillasLocal, n_amarillasVisita, partido_cancelado)

#Esto es por equipo:
def TiemposTarjetas(n_rojas, n_amarillas):
    n_rojas_1T=rd.randint(0,n_rojas)
    n_rojas_2T=n_rojas-n_rojas_1T
    
    n_amarillas_1T=rd.randint(0,n_amarillas)
    n_amarillas_2T=n_amarillas-n_amarillas_1T
    
    i=n_rojas_1T
    t_rojas_1T=[]
    while(i>0):
        i-=1
        t_rojas_1T.append(rd.randint(0,45))
    t_rojas_1T.sort()

    i=n_rojas_2T
    t_rojas_2T=[]
    while(i>0):
        i-=1
        t_rojas_2T.append(rd.randint(0,45))
    t_rojas_2T.sort()
    t_rojas=[t_rojas_1T,t_rojas_2T]

    
    i=n_amarillas_1T
    t_amarillas_1T=[]
    while(i>0):
        i-=1
        t_amarillas_1T.append(rd.randint(0,45))
    t_amarillas_1T.sort()

    i=n_amarillas_2T
    t_amarillas_2T=[]
    while(i>0):
        i-=1
        t_amarillas_2T.append(rd.randint(0,45))
    t_amarillas_2T.sort()
    t_amarillas=[t_amarillas_1T,t_amarillas_2T]

    return (t_rojas,t_amarillas)

def cambios(prob3,prob2,prob1):
    if rd.random()<prob3:
        n_cambios=3
    elif rd.random()<(prob3+prob2):
        n_cambios=2
    elif rd.random()<(prob3+prob2+prob1):
        n_cambios=1
    else:
        n_cambios=0
    posicion_cambios=[]
    t_cambios_1T=[]
    t_cambios_2T=[]
    if rd.random()<0.4:
        posicion_cambios=rd.sample(range(1,12),n_cambios)
    else:
        posicion_cambios=rd.sample(range(2,12),n_cambios)
    for i in range(n_cambios):
        if rd.random()<0.1:
            t_cambios_1T.append(rd.randint(0,45))
        else:
            t_cambios_2T.append(rd.randint(0,45))
    t_cambios_1T.sort()
    t_cambios_2T.sort()
    t_cambios=[t_cambios_1T,t_cambios_2T]
    return (posicion_cambios,t_cambios)

#Para un equipo en específico. 
def jTarjetas(n_rojas, n_amarillas):
    jAmarillas=[]
    for i in range(n_amarillas):
        jAmarillas.append(rd.randint(1,11))
    jRojas=rd.sample(range(1,12),n_rojas)
#jRojas.append(rd.randint(1,11))
    
    return (jAmarillas,jRojas)

#Se asignan los nombres de los jugadores que metieron gol (respetando los cambios de jugadores).
#La asignación es por equipo.
def AsignarJugGoles(jGoles, t_goles, pos_cambios, t_cambios, plantilla):
    jGoles_nombres=[]
    for n_jug in range(len(jGoles)):
        if n_jug<len(t_goles[0]):
            tgol=t_goles[0][n_jug]
        else:
            tgol=t_goles[1][n_jug-len(t_goles[0])]+1000
        
        ncambio=-1
        tcambio=0
        try:
            ncambio=pos_cambios.index(jGoles[n_jug])
        except ValueError:
            pass
            #print("El jugador no metió gol.")

        if ncambio<0:
            pass
            #print("no paso nada")
        else:
            if len(plantilla[ncambio+1][0])>0:
                tcambio=plantilla[ncambio+1][0][0]
            else:
                tcambio=plantilla[ncambio+1][1][0]+1000
    
        if ncambio==-1:
            jGoles_nombres.append(plantilla[0][0][1][jGoles[n_jug]])
        elif tgol<tcambio:
            jGoles_nombres.append(plantilla[0][0][1][jGoles[n_jug]])
        else:
            if len(plantilla[ncambio+1][0])>0:
                jGoles_nombres.append(plantilla[ncambio+1][0][1][jGoles[n_jug]])
            else:
                jGoles_nombres.append(plantilla[ncambio+1][1][1][jGoles[n_jug]])
    return jGoles_nombres

#Se asignan los nombres de los jugadores que recibieron alguna tarjeta (respetando los cambios de jugadores).
#La asignación es por equipo.
def AsignarJugTarjetas(jTarjetas, t_Tarjetas, pos_cambios, t_cambios, plantilla):
    jTarjetas_nombres=[]
    for n_jug in range(len(jTarjetas)):
        if n_jug<len(t_Tarjetas[0]):
            tgol=t_Tarjetas[0][n_jug]
        else:
            tgol=t_Tarjetas[1][n_jug-len(t_Tarjetas[0])]+1000
        
        ncambio=-1
        tcambio=0
        try:
            ncambio=pos_cambios.index(jTarjetas[n_jug])
        except ValueError:
            pass
            #print("El jugador no metió gol.")

        if ncambio<0:
            pass
            #print("no paso nada")
        else:
            if len(plantilla[ncambio+1][0])>0:
                tcambio=plantilla[ncambio+1][0][0]
            else:
                tcambio=plantilla[ncambio+1][1][0]+1000
    
        if ncambio==-1:
            jTarjetas_nombres.append(plantilla[0][0][1][jTarjetas[n_jug]])
        elif tgol<tcambio:
            jTarjetas_nombres.append(plantilla[0][0][1][jTarjetas[n_jug]])
        else:
            if len(plantilla[ncambio+1][0])>0:
                jTarjetas_nombres.append(plantilla[ncambio+1][0][1][jTarjetas[n_jug]])
            else:
                jTarjetas_nombres.append(plantilla[ncambio+1][1][1][jTarjetas[n_jug]])
    return jTarjetas_nombres

#Genera las plantillas en función del tiempo en el que se generan los cambios de jugadores:
def TPlantillas(Equipo, t_cambios, pos_cambios):
    Titulares=plant.plantillas_tit[Equipo]
    Titulares_t=Titulares.copy()
    Suplentes=plant.plantillas_sup[Equipo]
    plantilla=[[[0,Titulares],[]]]
    
    for i in range(3):
        if i<len(t_cambios[0]):
            Titulares_t[pos_cambios[i]]=Suplentes[pos_cambios[i]]
            plantilla.append([[t_cambios[0][i], Titulares_t],[]])
            Titulares_t=Titulares_t.copy()
        elif i-len(t_cambios[0])<len(t_cambios[1]):
            Titulares_t[pos_cambios[i]]=Suplentes[pos_cambios[i]]
            plantilla.append([[],[t_cambios[1][i-len(t_cambios[0])], Titulares_t]])
            Titulares_t=Titulares_t.copy()
        else:
            plantilla=plantilla

    return plantilla

#Función que hace que los jugadores que tengan doble amarilla instantáneamente tengan roja:
def DobleAmarilla_Roja(jAmarillas_nombres, jRojas_nombres,t_rojas,t_amarillas):
    #Generao una lista con los nombres de los jugadores que aparecen al menos 2 veces con amarilla:
    hola=list(dict.fromkeys([x for x in jAmarillas_nombres if jAmarillas_nombres.count(x)>=2]))
    adios=[]
    #Adios tiene las posiciones relativas de los jugadores según aparecen en la lista de tarjetas amarillas (solo jugadores con 2 de estas tarjetas al menos)
    #Por ejemplo, si la lista de jugadores con amarilla es: [A, B, A]
    #adios será igual a [0,2], ya que "A" aparece en posición 0 y 1 de la lista mencionada en la línea anterior.
    for k in hola:
        adios.append([i for i ,x in enumerate(jAmarillas_nombres) if x==k] )
    for i in range(len(adios)):
        entro=0
        #Chequeo si el jugador recibió su segunda amarilla en el primer tiempo. De ser el caso se asignan los jugadores y los tiempos como debe de ser ;)
        if adios[i][-1]<len(t_amarillas[0]):
            #Se chequea si no hay rojas asignadas en el primer tiempo. De ser este el caso, se hace un append:
            if len(t_rojas[0])==0:
                t_rojas[0].append(t_amarillas[0][adios[i][-1]])
                jRojas_nombres.insert(0,hola[i])
                entro=1
            else:
            #Si ya hay rojas asignadas en el primer tiempo:
                for iterador in range(len(t_rojas[0])):
                    if t_rojas[0][iterador]>t_amarillas[0][adios[i][-1]]:
                        t_rojas[0].append(t_amarillas[0][adios[i][-1]])
                        jRojas_nombres.insert(iterador, hola[i])
                        entro=1
                if entro==0:
                    t_rojas[0].append(t_amarillas[0][adios[i][-1]])
                    jRojas_nombres.insert(iterador+1, hola[i])
        else:
            if len(t_rojas[1])==0:
                t_rojas[1].append(t_amarillas[1][adios[i][-1]-len(t_amarillas[0])])
                jRojas_nombres.insert(len(t_rojas[0]),hola[i])
                entro=1
            else:
                for iterador in range(len(t_rojas[1])):
                    if t_rojas[1][iterador]>t_amarillas[1][adios[i][-1]-len(t_amarillas[0])]:
                        t_rojas[1].append(t_amarillas[1][adios[i][-1] - len(t_amarillas[0])])
                        jRojas_nombres.insert(iterador+len(t_rojas[1]), hola[i])
                        entro=1
                if entro==0:
                    t_rojas[1].append(t_amarillas[1][adios[i][-1] - len(t_amarillas[0])])
                    jRojas_nombres.insert(iterador+1+len(t_rojas[1]), hola[i])
    return (jRojas_nombres,t_rojas)

def TablaResultado(scoreLocal, scoreVisita, equipoLocal,equipoVisita,jGolesLocal_nombres, jGolesVisita_nombres, t_golesLocal, t_golesVisita, resultado , pos_cambiosLocal, t_cambiosLocal,pos_cambiosVisita,t_cambiosVisita, t_rojasLocal,t_amarillasLocal, t_rojasVisita,t_amarillasVisita, jAmarillasLocal_nombres, jRojasLocal_nombres,jAmarillasVisita_nombres,jRojasVisita_nombres):
    resultado_final=resultado
    if scoreLocal>0:
        resultado_final=resultado_final+"\nGoles:\n   "+equipoLocal
        for i in range(len(jGolesLocal_nombres)):
            if i<len(t_golesLocal[0]): #Goles del primer tiempo
                if rd.random()< prob_penal:
                    resultado_final=resultado_final+"\n   "+jGolesLocal_nombres[i]+"\t"+str(t_golesLocal[0][i])+"' 1T (P)"
                else:
                    resultado_final = resultado_final + "\n   " + jGolesLocal_nombres[i] + "\t" + str(t_golesLocal[0][i]) + "' 1T"
            else: #Goles del segundo tiempo
                if rd.random() < prob_penal:
                    resultado_final=resultado_final+"\n   "+jGolesLocal_nombres[i]+"\t"+str(t_golesLocal[1][i-len(t_golesLocal[0])])+"' 2T (P)"
                else:
                    resultado_final=resultado_final+"\n   "+jGolesLocal_nombres[i]+"\t"+str(t_golesLocal[1][i-len(t_golesLocal[0])])+"' 2T"
    if scoreVisita>0:
        if scoreLocal==0:
            resultado_final=resultado_final+"\nGoles:\n   "+equipoVisita
        else:  
            resultado_final=resultado_final+"\n\n   "+equipoVisita
        for i in range(len(jGolesVisita_nombres)):
            if i<len(t_golesVisita[0]): #Goles del primer tiempo
                #Chance de que un gol haya sido de penal:
                if rd.random() < prob_penal:
                    resultado_final=resultado_final+"\n   "+jGolesVisita_nombres[i]+"\t"+str(t_golesVisita[0][i])+"' 1T (P)"
                else:
                    resultado_final = resultado_final + "\n   " + jGolesVisita_nombres[i] + "\t" + str(t_golesVisita[0][i]) + "' 1T"
            else: #Goles del segundo tiempo
                if rd.random() < prob_penal:
                    resultado_final=resultado_final+"\n   "+jGolesVisita_nombres[i]+"\t"+str(t_golesVisita[1][i-len(t_golesVisita[0])])+"' 2T (P)"
                else:
                    resultado_final=resultado_final+"\n   "+jGolesVisita_nombres[i]+"\t"+str(t_golesVisita[1][i-len(t_golesVisita[0])])+"' 2T"

    #Se añade un texto que muestra los cambios que hubo en el partido:
    resultado_final = resultado_final + "\n\n\nCambios:"
    resultado_final = resultado_final + "\n\t"+equipoLocal
    if len(pos_cambiosLocal)==0:
        resultado_final = resultado_final + "\n\t No realizó cambios"
    else:
        for i in range(len(pos_cambiosLocal)):
            try:
                resultado_final=resultado_final+"\n\t"+plant.plantillas_sup[equipoLocal][pos_cambiosLocal[i]].rstrip()+" por "+plant.plantillas_tit[equipoLocal][pos_cambiosLocal[i]]+"\t"+str(t_cambiosLocal[0][i])+"' 1T"
            except IndexError:
                resultado_final=resultado_final+"\n\t"+plant.plantillas_sup[equipoLocal][pos_cambiosLocal[i]].rstrip()+" por "+plant.plantillas_tit[equipoLocal][pos_cambiosLocal[i]]+"\t"+str(t_cambiosLocal[1][i-len(t_cambiosLocal[0])])+"' 2T"
        resultado_final = resultado_final + "\n\n\t"+equipoVisita
    if len(pos_cambiosVisita) == 0:
            resultado_final = resultado_final + "\n\t No realizó cambios"
    else:
        for j in range(len(pos_cambiosVisita)):
            try:
                resultado_final=resultado_final+"\n\t"+plant.plantillas_sup[equipoVisita][pos_cambiosVisita[j]].rstrip()+" por "+plant.plantillas_tit[equipoVisita][pos_cambiosVisita[j]]+"\t"+str(t_cambiosVisita[0][j])+"' 1T"
            except IndexError:
                resultado_final=resultado_final+"\n\t"+plant.plantillas_sup[equipoVisita][pos_cambiosVisita[j]].rstrip()+" por "+plant.plantillas_tit[equipoVisita][pos_cambiosVisita[j]]+"\t"+str(t_cambiosVisita[1][j-len(t_cambiosVisita[0])])+"' 2T"

    #Se añade un texto que muestra las tarjetas AMARILLAS que hubo en el partido:
    resultado_final = resultado_final + "\n\n\nTarjetas Amarillas:"
    resultado_final = resultado_final + "\n\t"+equipoLocal
    if len(jAmarillasLocal_nombres)==0:
        resultado_final = resultado_final + "\n\tSin amarillas"
    else:
        for i in range(len(jAmarillasLocal_nombres)):
            try:
                resultado_final=resultado_final+"\n\t"+jAmarillasLocal_nombres[i]+str(t_amarillasLocal[0][i])+"' 1T"
            except IndexError:
                resultado_final=resultado_final+"\n\t"+jAmarillasLocal_nombres[i]+str(t_amarillasLocal[1][i-len(t_amarillasLocal[0])])+"' 2T"
    resultado_final = resultado_final + "\n\n\t"+equipoVisita
    if len(jAmarillasVisita_nombres)==0:
        resultado_final = resultado_final + "\n\tSin amarillas"
    else:
        for i in range(len(jAmarillasVisita_nombres)):
            try:
                resultado_final=resultado_final+"\n\t"+jAmarillasVisita_nombres[i]+str(t_amarillasVisita[0][i])+"' 1T"
            except IndexError:
                resultado_final=resultado_final+"\n\t"+jAmarillasVisita_nombres[i]+str(t_amarillasVisita[1][i-len(t_amarillasVisita[0])])+"' 2T"

    #Se añade un texto que muestra las tarjetas ROJAS que hubo en el partido:
    resultado_final = resultado_final + "\n\n\nTarjetas Rojas:"
    resultado_final = resultado_final + "\n\t"+equipoLocal
    if len(jRojasLocal_nombres)==0:
        resultado_final = resultado_final + "\n\tSin rojas"
    else:
        for i in range(len(jRojasLocal_nombres)):
            try:
                resultado_final=resultado_final+"\n\t"+jRojasLocal_nombres[i]+str(t_rojasLocal[0][i])+"' 1T"
            except IndexError:
                resultado_final=resultado_final+"\n\t"+jRojasLocal_nombres[i]+str(t_rojasLocal[1][i-len(t_rojasLocal[0])])+"' 2T"
    resultado_final = resultado_final + "\n\n\t"+equipoVisita
    if len(jRojasVisita_nombres)==0:
        resultado_final = resultado_final + "\n\tSin rojas"
    else:
        for i in range(len(jRojasVisita_nombres)):
            try:
                resultado_final=resultado_final+"\n\t"+jRojasVisita_nombres[i]+str(t_rojasVisita[0][i])+"' 1T"
            except IndexError:
                resultado_final=resultado_final+"\n\t"+jRojasVisita_nombres[i]+str(t_rojasVisita[1][i-len(t_rojasVisita[0])])+"' 2T"

    return resultado_final
