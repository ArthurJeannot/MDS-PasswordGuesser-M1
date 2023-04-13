from .ManageCase import ManageCase

class Capitalize(ManageCase):
    def __init__(self, mots=[]):
        super().__init__(mots)
        
    def run(self):
        res = []
        for mot in self.mots:
            res.append(mot.capitalize())
        return list(set(res))