import itertools

class PasswordGenerator:
    def __init__(self, elements):
        self.elements = elements

    def generate(self, nb_combinations):
        combinations = []
        for r in range(1, nb_combinations + 1):
            combinations.extend([''.join(p) for p in itertools.permutations(self.elements, r)])
        return combinations
    
    @property
    def elements(self):
        return self.__elements

    @elements.setter
    def elements(self, value):
        self.__elements = value or []