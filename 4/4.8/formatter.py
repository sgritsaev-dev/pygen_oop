from functools import singledispatchmethod

class Formatter:
    
    @singledispatchmethod
    @staticmethod
    def format(data):
        raise TypeError('Аргумент переданного типа не поддерживается')
    
    @format.register(int)
    @staticmethod
    def _int_format(data):
        print(f'Целое число: {data}')
    
    @format.register(float)
    @staticmethod
    def _float_format(data):
        print(f'Вещественное число: {data}')
    
    @format.register(list)
    @staticmethod
    def _list_format(data):
        print(f'''Элементы списка: {', '.join(str(el) for el in data)}''')
    
    @format.register(tuple)
    @staticmethod
    def _tuple_format(data):
        print(f'''Элементы кортежа: {', '.join(str(el) for el in data)}''')
    
    @format.register(dict)
    @staticmethod
    def _dict_format(data):
        print(f'''Пары словаря: {', '.join(str(el) for el in data.items())}''')
    