class Config:
    def __init__(self):
        self.leet = {
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
        self.__mots = ['StarWars'] #Seulement si test, sinon pris du formulaire (.env)
        self.__dates = ['2022-12-18'] #Pareil

    def _get_mots(self):
        return self.__mots

    def _get_dates(self):
        return self.__dates 