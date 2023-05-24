import unicodedata
from ..ManageElement import ManageElement

class Accentless(ManageElement):
    def __init__(self, mots=[]):
        super().__init__(mots)
        
    def _run(self):
        res = []
        for mot in self.elements:
            mot = unicodedata.normalize('NFKD', mot).encode('ASCII', 'ignore').decode('utf-8')
            res.append(mot)
        return list(set(res))