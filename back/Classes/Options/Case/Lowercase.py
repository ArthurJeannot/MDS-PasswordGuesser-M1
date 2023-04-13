from ..ManageWord import ManageWord

class Lowercase(ManageWord):
    def __init__(self, mots=[]):
        super().__init__(mots)
        
    def _run(self):
        res = []
        for mot in self.mots:
            res.append(mot.lower())
        return list(set(res))