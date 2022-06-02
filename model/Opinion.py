from model.Emoticono import Emoticono
from model.Usuario import Usuario


class Opinion:

    def __init__(self, Id, descripcion, fecha, id_empresa, id_experiencia, titulo, numero_likes, like):
        self.Id = Id
        self.Descripcion = descripcion
        self.Emoticono = Emoticono(-1, "DESDE APP GESTION INCOMPLETA")  # TODO
        self.Fecha = fecha
        self.Autor = Usuario(-1)  # TODO
        self.Id_Empresa = id_empresa
        self.Id_Experiencia = id_experiencia
        self.Titulo = titulo
        self.Numero_Likes = numero_likes
        self.Like = like

    @staticmethod
    def to_dict_data(opinion):
        return {
            'Id': opinion.Id,
            'Descripcion': opinion.Descripcion,
            'Emoticono': Emoticono.to_dict_data(opinion.Emoticono),
            'Fecha': opinion.Fecha,
             # 'Autor': Usuario.to_dict_data(Usuario(2)),  # TODO
            'Id_Empresa': opinion.Id_Empresa,
            'Id_Experiencia': opinion.Id_Experiencia,
            'Titulo': opinion.Titulo,
            'Numero_Likes': opinion.Numero_Likes,
            'Like': opinion.Like
        }
