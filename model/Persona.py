from model.Sexo import Sexo
from model.Usuario import Usuario


class Persona(Usuario):

    def __init__(self):
        super().__init__()
        self.Dni = ""
        self.Nombre = ""
        self.Apellido1 = ""
        self.Apellido2 = ""
        self.Sexo = Sexo()
        self.Fecha_Nacimiento = ""

