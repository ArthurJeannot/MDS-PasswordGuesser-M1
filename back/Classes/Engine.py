from .Config import Config
from .Options.Case.Uppercase import Uppercase
from .Options.Case.Lowercase import Lowercase
from .Options.Case.Capitalize import Capitalize
from .Options.Case.Accentless import Accentless
from .Options.Leet.LeetMax import LeetMax
from .Options.Leet.LeetMin import LeetMin
class Engine:
    def __init__(self, config=None):
        self.config = config

    def run(self):
        #TODO: Récup les options choisi et n'appliquer que ceux la (Liste de config) > Ajouter des if pour chaque ajout d'élément
        elements = self.config.mots
        
        elements = list(set(elements + Uppercase(elements).possibility))
        elements = list(set(elements + Lowercase(elements).possibility))
        elements = list(set(elements + Capitalize(elements).possibility))
        elements = list(set(elements + Accentless(elements).possibility))
        
        elements = list(set(elements + LeetMin(elements).possibility))
        elements = list(set(elements + LeetMax(elements).possibility))

        
        print(elements)
        print("Nombre d'éléments :", len(elements))
        
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
