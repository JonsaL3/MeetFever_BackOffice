from model.Usuario import Usuario


class Empresa(Usuario):

    def __init__(self):
        super().__init__()
        self.Nombre_Empresa = ""
        self.Cif = ""
        self.Direccion_Facturacion = ""
        self.Direccion_Fiscal = ""
        self.Nombre_Persona = ""
        self.Apellido1_Persona = ""
        self.Apellido2_Persona = ""
        self.Dni_Persona = ""
