from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont
#from PFB_Liga1 import *


alto=120
ancho=94
#scoreLocal_txt=str(scoreLocal)
#scoreVisita_txt=str(scoreVisita)
#e_local = str(Fixture[m][n][0])
#e_visita = str(Fixture[m][n][1])
#fecha_txt = str(m)

#Creamos el folder con las fotos de resultados de la fecha actual:
#print('\n \nEntro aquí')
#try:
#    os.mkdir(current_folder+"\Fotos_Fecha"+fecha_txt)
#    print("\n \nSe creó la carpeta con total y rotundo éxito. SABPEEE")
#except OSError:
#    print("\n \nNo pudo crearse la carpeta... quizás ya existía?")
#else:
#    print("\n \nLa carpeta ya había sido creada")



class Root(Toplevel):
    e_local=""
    e_visita=""
    scoreLocal=0
    scoreVisita=0
    fecha=0
    jGolesLoc_nombres=[]
    jGolesVis_nombres = []
    tgol_loc=[]
    tgol_vis=[]
    def __init__(self):
        super(Root, self).__init__()
        self.title("Resultado del partido")
        self.minsize(1200,1200)
        #self.wm_iconbitmap('D:\Program Files\Python\DLLs\py.ico')
        #self.configure(background='#4D4D4D')
        #self.creatCanvasImage()

    def creatCanvasImage(self,e_local, e_visita, scoreLocal, scoreVisita, fecha, jGolesLoc_nombres, tgol_loc, jGolesVis_nombres, tgol_vis):
        canvas =Canvas(self, bg="white", height =1200, width = 1200)

        canvas.pack(expand=YES, fill=BOTH)
        path_padre='D:\Google Drive\Daniel M\Codigos\Codigos míos\Facebook\Peruvian Football Bot\Fotos'
        marcador= Image.open(path_padre+'\marcador_base.png')
        equipo_loc = Image.open(path_padre+'\A_'+str(e_local)+'.png')
        equipo_local=equipo_loc.resize((ancho, alto), Image.LINEAR)
        equipo_local.save(path_padre + '\prueba2.png')
        equipo_local =  Image.open(path_padre+'\prueba2.png')
        equipo_vis = Image.open(path_padre+'\A_'+str(e_visita)+'.png')
        equipo_visita=equipo_vis.resize((ancho, alto), Image.LINEAR)
        equipo_visita.save(path_padre + '\prueba3.png')
        equipo_visita =  Image.open(path_padre+'\prueba3.png')
        area_l=(928,537,928+ancho,537+alto)
        area_v = (610, 637, 610 + ancho, 637 + alto)
        #Se pega el escudo del equipo local en la imagen de resultados:
        marcador.paste(equipo_local,area_l, equipo_local)
        #Se pega el escudo del equipo visitante en la imagen de resultados:
        marcador.paste(equipo_visita, area_v, equipo_visita)
        fnt = ImageFont.truetype('LSANS.ttf', 20)
        d = ImageDraw.Draw(marcador)
        #Se escribe el número de la fecha actual en la imagen de resultados:
        d.text((935, 55), "F E C H A     "+ str(fecha), font=fnt,fill=(240, 240, 240))
        fnt2=ImageFont.truetype('impact.ttf', 40)
        d = ImageDraw.Draw(marcador)
        #Se escribe el nombre del equipo local en la imagen de resultados:
        d.text((545, 592), str(e_local), font=fnt2,fill=(240, 240, 240))

        fnt3 = ImageFont.truetype('impact.ttf', 50)
        d = ImageDraw.Draw(marcador)
        #Se escribe el score del equipo local en la imagen de resultados:
        d.text((447, 587), str(scoreLocal), font=fnt3,fill=(240, 240, 240))

        fnt4=ImageFont.truetype('impact.ttf', 40)
        d = ImageDraw.Draw(marcador)
        #Se escribe el nombre del equipo visitante en la imagen de resultados:
        d.text((725, 680), str(e_visita), font=fnt4,fill=(240, 240, 240))
        fnt5 = ImageFont.truetype('impact.ttf', 50)
        d = ImageDraw.Draw(marcador)
        #Se escribe el score del equipo visitante en la imagen de resultados:
        d.text((1037, 675), str(scoreVisita), font=fnt5,fill=(240, 240, 240))


        #Se añaden los textos de los goles y los tiempos:
        temp_num=0
        for i in range(len(tgol_loc[0])):
            d.text((655-10*i, 542-30*i), str(tgol_loc[0][i])+'\' ' + str(jGolesLoc_nombres[i]), font=fnt, fill=(240, 240, 240))
            temp_num=i
        for j in range(len(tgol_loc[1])):
            d.text((655-10*(temp_num+1)-10*j, 542-30*(temp_num+1)-30*j), str(tgol_loc[1][j]+45)+'\' ' + str(jGolesLoc_nombres[j+len(tgol_loc[0])]), font=fnt, fill=(240, 240, 240))

        temp_num=0
        for i in range(len(tgol_vis[0])):
            d.text((725+10*i, 745+30*i), str(tgol_vis[0][i])+'\' ' + str(jGolesVis_nombres[i]), font=fnt, fill=(240, 240, 240))
            temp_num=i
        for j in range(len(tgol_vis[1])):
            d.text((725+10*(temp_num+1)+10*j, 745+30*(temp_num+1)+30*j), str(tgol_vis[1][j]+45)+'\' ' + str(jGolesVis_nombres[j+len(tgol_vis[0])]), font=fnt, fill=(240, 240, 240))


        canvas.image=ImageTk.PhotoImage(marcador)
        marcador.save('Resultados\Fotos_Fecha'+str(fecha)+'\A_ '+str(e_local)+' vs '+str(e_visita)+'.png')
        canvas.create_image(0,0, image=canvas.image, anchor='nw')



