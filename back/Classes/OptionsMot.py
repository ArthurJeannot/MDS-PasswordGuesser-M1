import unicodedata
import itertools


class OptionsMot:
    def __init__(self, mots=[str], dict_leet={str}):
        self.mots = mots
        self.dict_leet = dict_leet

    def apply_all_options(self):
        self.uppercase()
        self.lowercase()
        self.capital()
        self.remove_accents()
        self.leetify()

    def uppercase(self):
        for mot in self._mots:
            self.___add_mot(mot.upper())

    def lowercase(self):
        for mot in self._mots:
            self.___add_mot(mot.lower())

    def capital(self):
        for mot in self._mots:
            self.___add_mot(mot.capitalize())

    def remove_accents(self):
        for mot in self._mots:
            mot = unicodedata.normalize('NFKD', mot).encode(
                'ASCII', 'ignore').decode('utf-8')
            self.___add_mot(mot)


    def leetify(self):
        leet_mots = []
        for mot in self.mots:
            leet_chars = []
       
            for char in mot:
                if char.lower() in self.dict_leet:
                    leet_chars.append([char.lower(), self.dict_leet[char.lower()]])
                else:
                    leet_chars.append([char])
            # Crée toutes les variantes possibles de chaque caractère leet
            variants = itertools.product(*leet_chars)
            for variant in variants:
                leet_mot = ''.join(variant)
                if leet_mot.islower() or leet_mot.isupper():
                    leet_mots.append(leet_mot)
                    
        for mot in leet_mots:
            self.___add_mot(mot)

    # Vérifie qu'il ne s'agit pas d'une chaine vide et qu'il y a pas de doublon avant ajout dans le tableau
    def ___add_mot(self, mot):
        if mot and mot not in self._mots:
            self._mots.append(mot)

# Getter / Setter
    @property
    def mots(self):
        return self._mots

    @mots.setter
    def mots(self, value):
        self._mots = value or []

    @property
    def dict_leet(self):
        return self._dict_leet

    @dict_leet.setter
    def dict_leet(self, value):
        self._dict_leet = value or {
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
