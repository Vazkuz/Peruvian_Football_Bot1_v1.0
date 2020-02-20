
import datetime

ahora=datetime.datetime.now()
print("Hora: "+str(ahora.hour)+":"+str(ahora.minute)+"."+str(ahora.second))
ahora = datetime.datetime.now()
maniana = ahora+datetime.timedelta(days=0) #Si se desea que sea al día siguiente: days=1, si se desea que sea en el mismo día days=0. Esto para cuando se retoma la simulación pasada la medianoche.

#PROGRAMAMOS AL BOT PARA QUE EJECUTE AL DÍA SIGUIENTE A LAS 10AM:
maniana_10am = datetime.datetime(maniana.year,maniana.month,maniana.day,10,00,00)

for n_for in range(10):
    if n_for + 1 < 10:
        print("entro entre partidos")
        mas_45min = maniana_10am + datetime.timedelta(minutes=45*(n_for+1))
        hora_mas45min = datetime.datetime(mas_45min.year, mas_45min.month, mas_45min.day, mas_45min.hour, mas_45min.minute,00)
        ahora = datetime.datetime.now()
        # time.sleep(t_entre_partidos)
        print("Terminó el partido número "+str(n_for+1))
        print("Hora: " + str(hora_mas45min.hour) + ":" + str(hora_mas45min.minute)+"."+str(hora_mas45min.second))