from ..ManageElement import ManageElement

class Uppercase(ManageElement):
    def __init__(self, mots=[]):
        super().__init__(mots)
        
    def _run(self):
        res = []
        for mot in self.elements:
            res.append(mot.upper())
        return list(set(res))