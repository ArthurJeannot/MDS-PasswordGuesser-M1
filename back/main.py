from Classes.Config import Config
from Classes.Engine import Engine


if __name__ == '__main__':
    config = Config(['Arthur'], ['2023-12-18'], None)
    # config._add_mot('Pérennité')
    engine = Engine(config)
    engine.run()