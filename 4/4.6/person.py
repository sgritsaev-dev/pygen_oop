class Person:
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname
    @property
    def fullname(self):
        return f'{self.name} {self.surname}'
    @fullname.setter
    def fullname(self, fullname):
        name, surname = fullname.split()
        self.name= name
        self.surname=surname
    


person = Person('Джон', 'Маккарти')

person.fullname = 'Алан Тьюринг'
print(person.name)
print(person.surname)