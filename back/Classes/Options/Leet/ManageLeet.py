from ..ManageElement import ManageElement
import itertools

class ManageLeet(ManageElement):    
    def __init__(self, elements=[]):
        super().__init__(elements)
        
    def _run(self):
        res = []
        for mot in self.elements:
            leet_chars = []
            
            for char in mot:
                if char in self.dict_leet:
                    leet_chars.append([char, self.dict_leet[char]])
                else:
                    leet_chars.append([char])
                
            # Crée toutes les variantes possibles de chaque caractère leet
            variants = itertools.product(*leet_chars)
            for variant in variants:
                res.append(''.join(variant))
        return list(set(res))
    
# Getter / Setter        
    @property
    def dict_leet(self):
        return self._dict_leet

    @dict_leet.setter
    def dict_leet(self, value):
        self._dict_leet = value
