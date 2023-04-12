from Config import Config
from OptionsMot import OptionsMot


class Engine:
    def __init__(self, config=None):
        self.config = config

    def run(self):
        mots = self.config.mots
        options_mot = OptionsMot(mots)
        options_mot.apply_all_option()
        print(options_mot.mots)

# Getter / Setter
    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, value):
        self._config = value or Config()


if __name__ == '__main__':
    config = Config(['Arthur'], ['2022-12-18'], None)
    # config._add_mot('Pérennité')
    engine = Engine(config)
    engine.run()
