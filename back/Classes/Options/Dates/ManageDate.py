from datetime import datetime
from ..ManageElement import ManageElement

class ManageDate(ManageElement):    
    def __init__(self, elements=[]):
        dates = []
        for date in list(set(elements)):
            dates.append(datetime.strptime(date, '%Y-%m-%d'))
        self.dates = dates
        super().__init__(elements)
        
# Getter / Setter
    @property
    def dates(self):
        return self._dates

    @dates.setter
    def dates(self, value = []):
        self._dates = value