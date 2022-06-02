from model.Sexo import Sexo
from model.Usuario import Usuario


class Persona(Usuario):

    # all args constructor
    def __init__(self, Dni, Nombre, Apellido1, Apellido2, Sexo, Fecha_Nacimiento, id, correo, contrasena, nick, foto_perfil, foto_fondo, telefono, frase):
        super().__init__(id, correo, contrasena, nick, foto_perfil, foto_fondo, telefono, frase)
        self.Dni = Dni
        self.Nombre = Nombre
        self.Apellido1 = Apellido1
        self.Apellido2 = Apellido2
        self.Sexo = Sexo
        self.Fecha_Nacimiento = Fecha_Nacimiento

    @staticmethod
    def to_dict_data(persona: 'Persona') -> dict:
        super().to_dict_data(persona)
        dict_data = Usuario.to_dict_data(persona)
        dict_data['Dni'] = persona.Dni
        dict_data['Nombre'] = persona.Nombre
        dict_data['Apellido1'] = persona.Apellido1
        dict_data['Apellido2'] = persona.Apellido2
        dict_data['Sexo'] = Sexo.to_dict_data(persona.Sexo)
        dict_data['Fecha_Nacimiento'] = persona.Fecha_Nacimiento
        return dict_data

