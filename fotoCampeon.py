from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont
import PTC


alto=156
ancho=122

x=416
y=350


class Root3(Toplevel):
    #Creamos la tabla de posiciones que será, por defecto, un objeto básico de la clase Equipo
    t_posiciones=PTC.Equipo
    def __init__(self):
        #Esto lo saqué de internet, no recuerdo qué hace xd
        super(Root3, self).__init__()
        self.title("Resultado - Campeón")
        self.minsize(1200,1200)

    def creatCanvasImage(self, e_campeon):
        canvas =Canvas(self, bg="white", height =1200, width = 1200)
        fnt = ImageFont.truetype('impact.ttf', 70)

        canvas.pack(expand=YES, fill=BOTH)
        #Path del cual sacaremos la foto base
        path_padre='D:\Google Drive\Daniel M\Codigos\Codigos míos\Facebook\Peruvian Football Bot\Fotos'
        #Ubicación de la foto base:
        marcador= Image.open(path_padre+'\campeon_base.png')
        #Calculo el tamaño de la foto (lo usaré después)
        width, height = marcador.size
        #Genero el texto con el nombre del equipo, partidos jugados, ganados, empatados, perdidos, etc de estadísticas:
        equipo_camp = Image.open(path_padre + '\A_' + str(e_campeon) + '.png')
        equipo_campeon = equipo_camp.resize((ancho, alto), Image.LINEAR)
        equipo_campeon.save(path_padre + '\prueba3.png')
        equipo_campeon = Image.open(path_padre + '\prueba3.png')
        area_c = (416, 650, 416 + ancho, 650 + alto)
        marcador.paste(equipo_campeon, area_c, equipo_campeon)
        d = ImageDraw.Draw(marcador)
        w,h=d.textsize(e_campeon.upper(), font=fnt)
        d.text(((width-w)/2+1, y), e_campeon.upper(), font=fnt, fill=(0, 0, 0))
        d.text(((width-w)/2-1, y), e_campeon.upper(), font=fnt, fill=(0, 0, 0))
        d.text(((width-w)/2, y+1), e_campeon.upper(), font=fnt, fill=(0, 0, 0))
        d.text(((width-w)/2, y-1), e_campeon.upper(), font=fnt, fill=(0, 0, 0))
        d.text(((width-w)/2, y), e_campeon.upper(), font=fnt, fill=(205, 133, 63))
        #Se añaden los textos de los goles y los tiempos:

        canvas.image=ImageTk.PhotoImage(marcador)
        marcador.save('Resultados\Fotos_Final\Resultado_Campeon.png')
        canvas.create_image(0,0, image=canvas.image, anchor='nw')




