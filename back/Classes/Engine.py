from Config import Config
from OptionsMot import OptionsMot
from OptionsDate import OptionsDate

class Engine:
    def __init__(self, config=None):
        self.config = config

    def run(self):
        
        # Traitements des mots
        mots = self.config.mots
        options_mot = OptionsMot(mots)
        options_mot.apply_all_options()
        # print(options_mot.mots)
        
        # Triatement des dates
        dates = self.config.dates
        options_date = OptionsDate(dates)
        options_date.apply_all_options()
        print(options_date.dates)
        

# Getter / Setter
    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, value):
        self._config = value or Config()


if __name__ == '__main__':
    config = Config(['Arthur'], ['2023-12-18'], None)
    # config._add_mot('Pérennité')
    engine = Engine(config)
    engine.run()
