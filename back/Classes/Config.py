class Config:
    def __init__(self, mots=[], dates=[], dict_leet={}):
        self.mots = mots
        self.dates = dates
        self.dict_leet = dict_leet

    def _add_mot(self, mot):
        if mot and mot not in self.mots:
            self.__mots.append(mot)

    def _add_date(self, date):
        if date and date not in self.dates:
            self.__dates.append(date)

# Getter / Setter
    @property
    def mots(self):
        return self.__mots

    @mots.setter
    def mots(self, value):
        self.__mots = value or []

    @property
    def dates(self):
        return self.__dates

    @dates.setter
    def dates(self, value):
        self.__dates = value or []

    @property
    def dict_leet(self):
        return self.__dict_leet

    @dict_leet.setter
    def dict_leet(self, value):
        self.__dict_leet = value or {
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
