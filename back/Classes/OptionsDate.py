class OptionsDate:
    def __init__(self, dates) :
        self._dates = dates
        self._months = []
        self._elements = []

    def _get_months(self):
        return self._months

    def _get_dates(self):
        return self._dates