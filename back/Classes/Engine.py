from .Config import Config
from .Options.OptionsMot import OptionsMot
from .Options.OptionsDate import OptionsDate

class Engine:
    def __init__(self, config=None):
        self.config = config

    def run(self):
        #TODO: Récup les options choisi et n'appliquer que ceux la
        
        
        # Traitements des mots
        mots = self.config.mots
        options_mot = OptionsMot(mots)
        print(options_mot.apply_all_options())
        
        # Traitement des dates
        # dates = self.config.dates
        # options_date = OptionsDate(dates)
        # options_date.apply_all_options()
        # print(options_date.dates)
        

# Getter / Setter
    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, value):
        self._config = value or Config()
