from model.Emoticono import Emoticono
from model.Usuario import Usuario


class Opinion:

    def __init__(self):
        self.id = -1
        self.Descripcion = ""
        self.Emoticono = Emoticono()
        self.Fecha = ""
        self.Autor = Usuario()
        self.Id_Empresa = -1
        self.Id_Experiencia = -1
        self.Titulo = ""
        self.Numero_Likes = -1
        self.Like = False
