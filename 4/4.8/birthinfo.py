import re
from datetime import date
from functools import singledispatchmethod


class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register(date)
    def _(self, birth_date):
        self.birth_date = birth_date

    @__init__.register(str)
    def _(self, birth_date):
        if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', birth_date):
            raise TypeError('Аргумент переданного типа не поддерживается')
        self.birth_date = date.fromisoformat(birth_date)

    @__init__.register(list)
    @__init__.register(tuple)
    def _(self, birth_date):
        self.birth_date = date(*birth_date)

    @property
    def age(self):
        age = date.today().year - self.birth_date.year - 1
        age += (date.today().month, date.today().day) >= (
            self.birth_date.month, self.birth_date.day)
        return age
