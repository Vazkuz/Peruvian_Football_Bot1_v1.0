import pickle

hola=open('D:\Google Drive\Daniel M\Codigos\Codigos míos\Facebook\Peruvian Football Bot\Backups\pback_ups_equipos.pkl','rb')

equipo = pickle.load(hola)

print(equipo[13].puntaje)
print(equipo[13].nom_dict)
