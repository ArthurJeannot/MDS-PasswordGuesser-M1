from .ManageLeet import ManageLeet

class LeetMin(ManageLeet):
    def __init__(self, mots=[]):
        super().__init__(mots)

    dict_leet = {
            'a': '4',
            'e': '3',
            'i': '1',
            'o': '0',
            'l': '1',
            's': '5',
            'b': '8',
            't': '7',
            'z': '2',
            'g': '6'
        }