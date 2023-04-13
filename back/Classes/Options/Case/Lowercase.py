from .ManageCase import ManageCase

class Lowercase(ManageCase):
    def __init__(self, mots=[]):
        super().__init__(mots)
        
    def run(self):
        res = []
        for mot in self.mots:
            res.append(mot.lower())
        return list(set(res))