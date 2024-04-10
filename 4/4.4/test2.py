class Cat:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):                           # сеттер, используется для изменения имени
        if isinstance(name, str) and name.isalpha():    # проверка имени перед заменой
            self.__name = name
        else:
            raise ValueError('Некорректное имя')


cat = Cat('Кемаль')
print(cat.get_name())

cat.set_name('Роджер')
print(cat.get_name())