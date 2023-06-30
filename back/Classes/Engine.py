from .Config import Config
from .Options.Case.Uppercase import Uppercase
from .Options.Case.Lowercase import Lowercase
from .Options.Case.Capitalize import Capitalize
from .Options.Case.Accentless import Accentless
from .Options.Leet.LeetMax import LeetMax
from .Options.Leet.LeetMin import LeetMin
from .Options.Dates.DayNumber import DayNumber
from .Options.Dates.MonthNumber import MonthNumber
from .Options.Dates.FourDigitsYear import FourDigitYear
from .Options.Dates.TwoDigitsYear import TwoDigitYears
from .Options.Dates.HumanMonth import HumanMonth
from .Options.SpecialChar import SpecialChar
from .PasswordGenerator import PasswordGenerator

class Engine:
    def __init__(self):
        self.config = Config()
                       
    def run(self):
        self.__init_config()
        guesser = PasswordGenerator(self.get_all_elements())
        combinaisons = guesser.generate(self.nb_combinaison)
        print('\n--------')
        print(f"Resultat:\n{combinaisons}\n\nNombre d'éléments : {len(combinaisons)}")

    def get_all_elements(self):
        dates = self.config.dates
        elements = self.config.mots        
        for option, value in self.config.options.items():
            if value:
                if option == 'uppercase':
                    elements = Uppercase.add_word_possibility(elements)
                elif option == 'lowercase':
                    elements = Lowercase.add_word_possibility(elements)
                elif option == 'capitalize':
                    elements = Capitalize.add_word_possibility(elements)
                elif option == 'accentless':
                    elements = Accentless.add_word_possibility(elements)
                elif option == 'leet_min':
                    elements = LeetMin.add_word_possibility(elements)
                elif option == 'leet_max':
                    elements = LeetMax.add_word_possibility(elements)
                elif option == 'day':
                    elements = DayNumber.add_dates_possibility(dates, elements)
                elif option == 'month':
                    elements = MonthNumber.add_dates_possibility(dates, elements)
                elif option == 'human_month':
                    elements = HumanMonth.add_dates_possibility(dates, elements)
                elif option == 'four_digit_year':
                    elements = FourDigitYear.add_dates_possibility(dates, elements)
                elif option == 'two_digit_year':
                    elements = TwoDigitYears.add_dates_possibility(dates, elements)
                elif option == 'special_char':
                    elements = SpecialChar.add_special_char(elements)
        return elements
    
    def __init_config(self):
        mots = input("Saisissez une liste de mots, séparés par des espaces (Vide si aucun mot)\n:").split()
        print('\n--------')
        dates = (input("Saisissez saisir une liste de dates (Format AAAA-MM-DD), séparées par des espaces (Vide si aucune date)\n:").split())
        print('\n--------')            
        disabled_options = (input(f"Choisissez les options a désactiver, séparés par des espaces (Vide si on garde toute les options):\n{list(Config.default_option().keys())}\n:").split())
        print('\n--------')
        if self.config.options['human_month'] and dates:
            lang = input(f'Choisissez votre langue pour les mois parmis cette liste (vide = fr):\n{HumanMonth.available_languages()}\n:')
            print('\n--------')
            HumanMonth.change_lang(lang)
        self.nb_combinaison = int(input("Veuillez indiquer le nombre de combinaison max (Vide pour voir la liste d'éléments sans combinaison)\n:") or 1)
        self.config.add_mots(mots)
        self.config.add_dates(dates)
        self.config.disable_option(disabled_options)

# Getter / Setter
    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, value):
        self._config = value or Config()

    @property
    def nb_combinaison(self):
        return self.__nb_combinaison

    @nb_combinaison.setter
    def nb_combinaison(self, value):
        self.__nb_combinaison = value or 1