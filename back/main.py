from Classes.Config import Config
from Classes.Engine import Engine


if __name__ == '__main__':
    config = Config(['Arthur'], ['2023-12-18'])
    
    config.enable_option(['OptionInexistante'])
    config.disable_option(['uppercase'])
    # config.reset_default_option()
    
    # config._add_mots(['Pérennité', 'éolienne'])
    engine = Engine(config)
    engine.run()