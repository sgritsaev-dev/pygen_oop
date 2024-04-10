class User:
    def __init__(self, name, age) -> None:
        if not(isinstance(name, str) and name.isalpha()):
            raise ValueError('Некорректное имя')
        self._name=name
        if not(isinstance(age, int) and 0<=age<110):
            raise ValueError('Некорректный возраст')
        self._age=age
    
    def get_name(self):
        return self._name
    
    def set_name(self, new_name):
        if not(isinstance(new_name, str) and new_name.isalpha()):
            raise ValueError('Некорректное имя')
        self._name=new_name

    def get_age(self):
        return self._age
    
    def set_age(self, new_age):
        if not(isinstance(new_age, int) and 0<=new_age<110):
            raise ValueError('Некорректный возраст')
        self._age=new_age

user = User('Гвидо', 67)

user.set_name('Тимур')
user.set_age(30)

print(user.get_name())
print(user.get_age())