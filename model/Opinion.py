from model.Emoticono import Emoticono
from model.Usuario import Usuario


class Opinion:

    def __init__(self, Id, descripcion, fecha, id_autor, emoticono, id_empresa, id_experiencia, titulo, numero_likes, like):
        self.Id = Id
        self.Descripcion = descripcion
        self.Emoticono = emoticono
        self.Fecha = fecha
        self.Autor = Usuario.usuario_factory_by_id(id_autor)
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
            'Id_Autor': opinion.Autor.Id,
            'Id_Empresa': opinion.Id_Empresa,
            'Id_Experiencia': opinion.Id_Experiencia,
            'Titulo': opinion.Titulo
        }
