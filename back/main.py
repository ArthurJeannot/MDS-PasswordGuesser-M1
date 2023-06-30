from Classes.Config import Config
from Classes.Engine import Engine
from Classes.Options.ManageElement import ManageElement


if __name__ == '__main__':
    # print(Config.default_option()) #Pour test si l'instanciation d'une classe abstraite est bloqué
    
    Engine().run()