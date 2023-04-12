from Config import Config
from OptionsMot import OptionsMot

class Engine:
    def __init__(self):
        self.config = Config()

    def run(self):
        # mots = self.config._get_mots()
        mots = ['arthur', 'Arthur']

        options_mot = OptionsMot(mots)
        options_mot.apply_all_option()
        elements = options_mot._elements
        options_mot._reset_element()
        # print(options_mot._elements)
        # for element in elements:
        #     print(element)

if __name__ == '__main__':
    engine = Engine()
    engine.run()



# from Config import Config
# from OptionsDate import OptionsDate
# from OptionsMot import OptionsMot

# # fichier .env
# # ENV = prod # || test

# # Nom variable
# # self.public = True
# # self._protected = True
# # self.__private = True


# class Engine:
#     def __init__(self, config) :
#         self.__config = config
#         self.set_attribute()


#     def set_attribute(self):
#         # self.__optionsDate = OptionsDate()
#         self.__optionsMot = OptionsMot(self.__config._get_mots())
#         self.__elements = []

#     def add_word(self, word):
#         self.__elements.append(word)

#     def run(self) :
#         # A refacto
#         self.mots.extend(self.optionsDate._get_months())
#         optionsMot = OptionsMot(mots)
#         optionsMot.uppercase()
#         optionsMot.lowercase()
#         optionsMot.capital()

#         print(self.__elements)

# # if not accentless_word == word

# # Permet de s'éxécuter uniquement si directement appeler depuis terminal
# if __name__ == '__main__':
#     Engine()