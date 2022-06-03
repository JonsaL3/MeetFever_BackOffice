from model.Empresa import Empresa


class Experiencia:

    def __init__(self):
        self.Id = -1
        self.Aforo = -1
        self.Descripcion = ""
        self.Empresa = Empresa("", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "")
        self.Fecha_Celebracion = ""
        self.Foto = ""
        self.Precio = -1.1
        self.Titulo = ""

    def __init__(self, Id, Aforo, Descripcion, Fecha_Celebracion, Foto, Precio, Titulo):
        self.Id = Id
        self.Aforo = Aforo
        self.Descripcion = Descripcion
        # TODO self.Empresa = Empresa
        self.Fecha_Celebracion = Fecha_Celebracion
        self.Foto = Foto
        self.Precio = Precio
        self.Titulo = Titulo

    def to_dict_data(self):
        return {
            'Id': self.Id,
            'Aforo': self.Aforo,
            'Descripcion': self.Descripcion,
             #'Empresa': Empresa.to_dict_data(),
            'Fecha_Celebracion': self.Fecha_Celebracion,
            'Foto': self.Foto,
            'Precio': self.Precio,
            'Titulo': self.Titulo
        }