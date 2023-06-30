from .ManageDate import ManageDate

class FourDigitYear(ManageDate):
    def __init__(self, dates=[]):
        super().__init__(dates)
        
    def _run(self):
        res = []
        for date in self.dates:
            res.append(str(date.year))
        return list(res)