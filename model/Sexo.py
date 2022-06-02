class Sexo:

    def __init__(self, Id: int, Sepso: str):
        self.Id = Id
        self.Sexo = Sepso

    @staticmethod
    def to_dict_data(sexo: 'Sexo'):
        return {
            'Id': sexo.Id,
            'Sexo': sexo.Sexo
        }
