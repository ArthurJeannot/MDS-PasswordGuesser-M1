from Classes.Config import Config
from Classes.Engine import Engine


if __name__ == '__main__':
    config = Config(['Arthur', 'éolienne'], ['2023-12-18'])
    
    print(config.options)
    
    config.enable_option(['Oui'])
    config.disable_option(['uppercase'])
    # config.reset_default_option()
    
    print(config.default_option)
    # config._add_mot('Pérennité')
    # engine = Engine(config)
    # engine.run()