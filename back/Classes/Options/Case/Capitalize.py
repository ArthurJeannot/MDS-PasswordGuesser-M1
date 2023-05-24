from ..ManageElement import ManageElement

class Capitalize(ManageElement):
    def __init__(self, mots=[]):
        super().__init__(mots)
        
    def _run(self):
        res = []
        for mot in self.elements:
            res.append(mot.capitalize())
        return list(set(res))