from .ManageDate import ManageDate

class TwoDigitYears(ManageDate):
    def __init__(self, dates=[]):
        super().__init__(dates)
        
    def _run(self):
        res = []
        for date in self.dates:
            res.append(str(date.year)[-2:])
        return list(res)
