from .ManageLeet import ManageLeet

class LeetMax(ManageLeet):
    def __init__(self, mots=[]):
        super().__init__(mots)
    
    dict_leet = {
            'A': '4',
            'E': '3',
            'I': '1',
            'O': '0',
            'L': '1',
            'S': '5',
            'B': '8',
            'T': '7',
            'Z': '2',
            'G': '6'
        }