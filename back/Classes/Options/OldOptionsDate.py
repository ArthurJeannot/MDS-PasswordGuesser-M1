#TODO, a refacto et faire pareil que leet et case

from datetime import datetime
from typing import List


class OptionsDate:
    #Les dates doivent être au format iso (YYYY-MM-DD)
    def __init__(self, dates: List[str], lang: str = 'fr'):
        self.dates_origin = dates
        self.dates = dates
        
        self.lang = lang.lower()

    def apply_all_options(self):
        print('')
        self.split_dates()
        self.use_numbers()
        self.use_human_language()
        self.use_two_digit_year()
        self.use_four_digit_year()

    def split_dates(self):
        elements = []
        for date in self.dates:
            elements.extend(date.split('-'))
        elements = list(set(elements))
        for element in elements:
            if len(element) > 0:
                self._add_element(element)

    def use_numbers(self):
        elements = []
        for date in self.dates:
            elements.extend(date.split('-'))
        for element in elements:
            if element.isnumeric():
                self._add_element(element)

    def use_human_language(self):
        months = {
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
        if self.lang not in months:
            return
        elements = []
        for date in self.dates:
            elements.extend(date.split('-'))
        for element in elements:
            if len(element) == 2:
                self._add_element(months[self.lang].get(element))

    def use_two_digit_year(self):
        elements = []
        for date in self.dates:
            elements.extend(date.split('-'))
        for element in elements:
            if len(element) == 2 and element.isnumeric():
                self._add_element(element)

    def use_four_digit_year(self):
        elements = []
        for date in self.dates:
            try:
                datetime.strptime(date, '%d/%m/%Y')
                elements.append(date[-4:])
            except ValueError:
                pass
        for element in elements:
            self._add_element(element)

    def _add_element(self, element: str):
        if element and element not in self.dates:
            self.dates.append(element)

    # Getter / Setter
    @property
    def dates(self):
        return self._dates

    @dates.setter
    def dates(self, value):
        self._dates = value or []
        
    @property
    def dates_origin(self):
        return self._dates

    @dates_origin.setter
    def dates_origin(self, value):
        self._dates_origin = value or []

    @property
    def lang(self):
        return self._lang

    @lang.setter
    def lang(self, value):
        self._lang = value.lower()