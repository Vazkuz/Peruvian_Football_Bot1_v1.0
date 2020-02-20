from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont
import PTC


alto=120
ancho=94


class Root2(Toplevel):
    #Creamos la tabla de posiciones que será, por defecto, un objeto básico de la clase Equipo
    t_posiciones=PTC.Equipo
    def __init__(self):
        #Esto lo saqué de internet, no recuerdo qué hace xd
        super(Root2, self).__init__()
        self.title("Tabla de posiciones")
        self.minsize(1200,1200)

    def creatCanvasImage(self, t_posiciones, fecha):
        canvas =Canvas(self, bg="white", height =1200, width = 1200)

        canvas.pack(expand=YES, fill=BOTH)
        #Path del cual sacaremos la foto base
        path_padre='D:\Google Drive\Daniel M\Codigos\Codigos míos\Facebook\Peruvian Football Bot\Fotos'
        #Ubicación de la foto base:
        marcador= Image.open(path_padre+'\A_tabla_posiciones_base.png')
        fnt = ImageFont.truetype('LSANS.ttf', 20)
        fnt2 = ImageFont.truetype('LSANS.ttf', 16)
        fntfecha = ImageFont.truetype('impact.ttf', 27)
        d = ImageDraw.Draw(marcador)

        #Genero el texto con el nombre del equipo, partidos jugados, ganados, empatados, perdidos, etc de estadísticas:
        for iii in range(len(t_posiciones)):
            txt_team = t_posiciones[iii].nom_dict
            txt_pj = t_posiciones[iii].p_jugados
            txt_pg = t_posiciones[iii].p_ganados
            txt_pe = t_posiciones[iii].p_empatados
            txt_pp = t_posiciones[iii].p_perdidos
            txt_gf = t_posiciones[iii].gfavor
            txt_gc = t_posiciones[iii].gcontra
            txt_dg = t_posiciones[iii].dif_goles
            txt_puts= t_posiciones[iii].puntaje
            d.text((175, 175+36.5*iii), txt_team, font=fnt, fill=(0, 0, 0))
            d.text((469-4*len(str(txt_pj)), 178+36.5*iii), str(txt_pj), font=fnt2, fill=(0, 0, 0))
            d.text((499-4*len(str(txt_pg)), 178 + 36.5 * iii), str(txt_pg), font=fnt2, fill=(0, 0, 0))
            d.text((529-4*len(str(txt_pe)), 178 + 36.5 * iii), str(txt_pe), font=fnt2, fill=(0, 0, 0))
            d.text((559-4*len(str(txt_pp)), 178 + 36.5 * iii), str(txt_pp), font=fnt2, fill=(0, 0, 0))
            d.text((589-4*len(str(txt_gf)), 178 + 36.5 * iii), str(txt_gf), font=fnt2, fill=(0, 0, 0))
            d.text((619-4*len(str(txt_gc)), 178 + 36.5 * iii), str(txt_gc), font=fnt2, fill=(0, 0, 0))
            d.text((654-4*len(str(txt_dg)), 178 + 36.5 * iii), str(txt_dg), font=fnt2, fill=(0, 0, 0))
            d.text((688-5*len(str(txt_puts)), 175 + 36.5 * iii), str(txt_puts), font=fnt, fill=(240, 240, 240))
            d.text((380,90), "FECHA "+ str(fecha),font=fntfecha, fill=(240, 240, 240))

        #Se añaden los textos de los goles y los tiempos:

        canvas.image=ImageTk.PhotoImage(marcador)
        marcador.save('Resultados\Fotos_Fecha'+str(fecha)+'\A_Tabla_Posiciones.png')
        canvas.create_image(0,0, image=canvas.image, anchor='nw')




