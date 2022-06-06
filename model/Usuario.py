class Usuario:

    # all args constructor
    def __init__(self, id, correo, contrasena, nick, foto_perfil, foto_fondo, telefono, frase):
        self.Id = id
        self.Correo = correo
        self.Contrasena = contrasena
        self.Nick = nick
        self.Foto_Perfil = foto_perfil
        self.Foto_Fondo = foto_fondo
        self.Telefono = telefono
        self.Frase = frase

    @staticmethod
    def usuario_factory_by_id(id_usuario: int) -> 'Usuario':
        return Usuario(id_usuario, "", "", "", "", "", "", "")

    @staticmethod
    def to_dict_data(usuario: 'Usuario') -> dict:
        return {
            "Id": usuario.Id,
            "Correo": usuario.Correo,
            "Contrasena": usuario.Contrasena,
            "Nick": usuario.Nick,
            "Foto_Perfil": usuario.Foto_Perfil,
            "Foto_Fondo": usuario.Foto_Fondo,
            "Telefono": usuario.Telefono,
            "Frase": usuario.Frase
        }
