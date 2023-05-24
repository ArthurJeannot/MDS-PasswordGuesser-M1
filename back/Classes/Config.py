class Config:
    def __init__(self, mots = [], dates = []):
        self.mots = list(set(mots))
        self.dates = list(set(dates))
        self.reset_default_option()

    def _add_mots(self, mots = []):
        for mot in mots:
            if mot and mot not in self.mots:
                self.mots.append(mot)

    def _add_dates(self, dates = []):
        for date in dates:
            if date and date not in self.dates:
                self.dates.append(date)
        
    # Limite l'accès a la liste d'options, permet d'éviter la modification des champs d'option
    # Les méthodes enable et disable permettent d'activer/désactiver les options présente dans la liste de base
    def enable_option(self, options = []):
        for key in options:
            if key in self.default_option.keys():
                self.options[key] = True
        
    def disable_option(self, options = []):
        for key in options:
            if key in self.default_option.keys():
                self.options[key] = False
            
    #Remet la liste de filtre a celle par défaut
    def reset_default_option(self):
        self.__options = self.default_option

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
    def mots(self):
        return self.__mots

    @mots.setter
    def mots(self, value):
        self.__mots = value or []
        
    @property
    def options(self):
        return self.__options
    
    @property
    def default_option(self):
        return {
            'uppercase' : True,
            'lowercase' : True,
            'accentless' : True,
            'capitalize' : True,
            'leet_max' : True,
            'leet_min' : True
        }