from .ManageDate import ManageDate

class HumanMonth(ManageDate):
    lang = 'fr'
    
    def __init__(self, dates=[]):
        super().__init__(dates)

    def _run(self):
        res = []
        month_dict = self.all_month_dict()[self.lang]
        
        for date in self.dates:
            month = str(date.month).zfill(2)  # Ajout de zéros initiaux au numéro du mois
            month_name = month_dict.get(month)
            if month_name:
                res.append(month_name)
        return res
    
    @classmethod
    def change_lang(cls, lang):
        if lang in cls.available_languages():
            cls.lang = lang

    @staticmethod
    def all_month_dict():
        return {
            'fr': {
                '01': 'janvier',
                '02': 'février',
                '03': 'mars',
                '04': 'avril',
                '05': 'mai',
                '06': 'juin',
                '07': 'juillet',
                '08': 'août',
                '09': 'septembre',
                '10': 'octobre',
                '11': 'novembre',
                '12': 'décembre'
            },
            'en': {
                '01': 'january',
                '02': 'february',
                '03': 'march',
                '04': 'april',
                '05': 'may',
                '06': 'june',
                '07': 'july',
                '08': 'august',
                '09': 'september',
                '10': 'october',
                '11': 'november',
                '12': 'december'
            }
        }

    @classmethod
    def available_languages(cls):
        return list(cls.all_month_dict().keys())