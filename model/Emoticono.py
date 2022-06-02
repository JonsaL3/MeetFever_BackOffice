class Emoticono:

    def __init__(self, Id: int, Emoji: str):
        self.Id = Id
        self.Emoji = Emoji

    def to_dict_data(self):
        return {
            'Id': self.Id,
            'Emoji': self.Emoji
        }



