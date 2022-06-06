from model.Empresa import Empresa


class Experiencia:

    def __init__(self, Id, Aforo, Descripcion, empresa: Empresa, Fecha_Celebracion, Foto, Precio, Titulo):
        self.Id = Id
        self.Aforo = Aforo
        self.Descripcion = Descripcion
        self.Empresa = empresa
        self.Fecha_Celebracion = Fecha_Celebracion
        self.Foto = Foto
        self.Precio = Precio
        self.Titulo = Titulo

    def to_dict_data(self):
        return {
            'Id': self.Id,
            'Aforo': self.Aforo,
            'Descripcion': self.Descripcion,
            'Empresa': Empresa.to_dict_data(self.Empresa),
            'Fecha_Celebracion': self.Fecha_Celebracion,
            'Foto': self.Foto,
            'Precio': self.Precio,
            'Titulo': self.Titulo
        }
