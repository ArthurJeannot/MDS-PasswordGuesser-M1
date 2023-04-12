import unicodedata

class OptionsMot:
    def __init__(self, mots = [], leet = None):
        self._elements = mots
        self._mots = mots
        self._leet = leet or {
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
        
    
    def apply_all_option(self):
        self.uppercase()
        self.lowercase()
        self.capital()
        self.remove_accents()
        self.leetify()

    def uppercase(self):
        for mot in self._mots:
            self.___add_element(mot.upper())
            
    def lowercase(self):
        for mot in self._mots:
            self.___add_element(mot.lower())

    def capital(self):
        for mot in self._mots:
            self.___add_element(mot.capitalize())

    def remove_accents(self):
        for mot in self._mots:
            mot = unicodedata.normalize('NFKD', mot).encode('ASCII', 'ignore').decode('utf-8')
            self.___add_element(mot) 
            
    def leetify(self):
        leet_elements = []
        for mot in self._mots:
            for c in mot:
                if c.lower() in self._leet:
                    mot = mot.replace(c, self._leet[c.lower()])
            leet_elements.append(mot)
        for element in leet_elements:
            self.___add_element(element)
            
# Vérifie qu'il n'y a pas de doublon avant ajout dans le tableau
    def ___add_element(self, mot):
        if mot not in self._elements:
                self._elements.append(mot)
            
# Reset la liste d'élément en enlevant tout les mots ajouter avec les filtres (également appeler lors de _set_mots)   
    def _reset_element(self):
        print(self.elements, self.mots)
        self._elements = self.mots
        print(self.elements)
        print('-----')
  
# Getter / Setter
    @property
    def mots(self):
        return self._mots or []
    
    @mots.setter
    def mots(self, value):
        self._mots = value or []
        self._reset_element()
        
    @property
    def leet(self):
        return self._leet or {}
    
    @leet.setter
    def leet(self, value):
        self._leet = value
        
    @property
    def elements(self):
        return self._elements or []