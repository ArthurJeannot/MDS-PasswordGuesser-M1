import unicodedata
from ..ManageWord import ManageWord

class Accentless(ManageWord):
    def __init__(self, mots=[]):
        super().__init__(mots)
        
    def _run(self):
        res = []
        for mot in self.mots:
            mot = unicodedata.normalize('NFKD', mot).encode('ASCII', 'ignore').decode('utf-8')
            res.append(mot)
        return list(set(res))