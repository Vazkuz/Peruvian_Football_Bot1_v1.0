

class Equipo:
    puntaje=0
    gfavor=0
    gcontra=0
    ult_res=0 #0: empate, 1: victoria, -1: derrota
    p_jugados=0
    p_ganados=0
    p_empatados=0
    p_perdidos=0
    dif_goles=0
    def __init__(self, nombre): #, img_ubicacion)
        self.nom_dict=nombre
        #self.ubicacion_img=img_ubicacion

    def victoria(self):
        self.puntaje+=3
        self.ult_res=1
        self.p_ganados+=1
        self.p_jugados+=1

    def empate(self):
        self.puntaje+=1
        self.ult_res=0
        self.p_empatados+=1
        self.p_jugados+=1

    def derrota(self):
        self.ult_res=-1
        self.p_perdidos+=1
        self.p_jugados+=1

    def marcador(self, goles, goles_contra):
        self.gfavor+=goles
        self.gcontra+=goles_contra

    def print_stats(self):
        print(str(self.nom_dict)+' tiene '+str(self.puntaje)+' puntos.')

    def f_dif_goles(self, goles, goles_contra):
        self.dif_goles+=goles-goles_contra

    def redefinir_info(self, p_ganados_n, p_empatados_n, p_perdidos_n, gfavor_n, gcontra_n, ult_res_n):
        self.puntaje = p_ganados_n*3+p_empatados_n
        self.gfavor = gfavor_n
        self.gcontra = gcontra_n
        self.ult_res = ult_res_n  # 0: empate, 1: victoria, -1: derrota
        self.p_jugados = p_ganados_n+p_empatados_n+p_perdidos_n
        self.p_ganados = p_ganados_n
        self.p_empatados = p_empatados_n
        self.p_perdidos = p_perdidos_n
        self.dif_goles = gfavor_n-gcontra_n

