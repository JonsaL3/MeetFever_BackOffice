from model.Usuario import Usuario


class Empresa(Usuario):

    def __init__(self, id, correo, contrasena, nick, foto_perfil, foto_fondo, telefono, frase, nombre_empresa, cif, direccion_facturacion, direccion_fiscal, nombre_persona, apellido1_persona, apellido2_persona, dni_persona):
        super().__init__(id, correo, contrasena, nick, foto_perfil, foto_fondo, telefono, frase)
        self.Nombre_Empresa = nombre_empresa
        self.Cif = cif
        self.Direccion_Facturacion = direccion_facturacion
        self.Direccion_Fiscal = direccion_fiscal
        self.Nombre_Persona = nombre_persona
        self.Apellido1_Persona = apellido1_persona
        self.Apellido2_Persona = apellido2_persona
        self.Dni_Persona = dni_persona

    @staticmethod
    def to_dict_data(empresa: 'Empresa') -> dict:
        dict_data = Usuario.to_dict_data(empresa)
        dict_data['Nombre_Empresa'] = empresa.Nombre_Empresa
        dict_data['Cif'] = empresa.Cif
        dict_data['Direccion_Facturacion'] = empresa.Direccion_Facturacion
        dict_data['Direccion_Fiscal'] = empresa.Direccion_Fiscal
        dict_data['Nombre_Persona'] = empresa.Nombre_Persona
        dict_data['Apellido1_Persona'] = empresa.Apellido1_Persona
        dict_data['Apellido2_Persona'] = empresa.Apellido2_Persona
        dict_data['Dni_Persona'] = empresa.Dni_Persona
        return dict_data

