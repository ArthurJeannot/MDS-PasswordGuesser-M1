#WIP A éclater en plusieurs classes

import unicodedata
import itertools

class OptionsMot:
    def __init__(self, mots=[], dict_leet={}):
        self.mots = mots
        self.dict_leet = dict_leet

    def apply_all_options(self, mots=[]):
        elements = mots if mots else self.mots
               
        elements = list(set(elements + self.uppercase(elements)))
        elements = list(set(elements + self.lowercase(elements)))
        elements = list(set(elements + self.capital(elements)))
        elements = list(set(elements + self.remove_accents(elements)))
        elements = list(set(elements + self.leetify(elements)))
        
        return elements

    def uppercase(self, mots=[]):       
        elements = mots if mots else self.mots
        res = []
        for mot in elements:
            res.append(mot.upper())
        return list(set(res))

    def lowercase(self, mots=[]):
        elements = mots if mots else self.mots
        res = []
        for mot in elements:
            res.append(mot.lower())
        return list(set(res))

    def capital(self, mots = []):
        elements = mots if mots else self.mots
        res = []
        for mot in elements:
            res.append(mot.capitalize())
        return list(set(res))

    def remove_accents(self, mots = []):
        elements = mots if mots else self.mots
        res = []
        for mot in elements:
            mot = unicodedata.normalize('NFKD', mot).encode(
                'ASCII', 'ignore').decode('utf-8')
            res.append(mot)
        return list(set(res))


    def leetify(self, mots = []):
        elements = mots if mots else self.mots
        res = []
        for mot in elements:
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
                    res.append(leet_mot)
        return list(set(res))

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
