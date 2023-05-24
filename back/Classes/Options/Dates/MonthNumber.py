from .ManageDate import ManageDate

class MonthNumber(ManageDate):
    def __init__(self, dates=[]):
        super().__init__(dates)
        
    def _run(self):
        res = []
        for date in self.dates:
            res.append(str(date.month))
        return list(res)