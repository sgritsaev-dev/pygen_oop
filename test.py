class Dog:
    __color = "color"
    def __init__(self, color:str, name:str, sex:str) -> None:
        self.__color = color
        self._name = name
        self.sex = sex

    @property
    def color(self):
        return self.__color

    @classmethod
    def change_color(cls, new_color):
        cls.__color = new_color

dog1 = Dog('blue' ,'Denis', 'Male')
dog2 = Dog('grey' , 'Sergei', 'Male')

Dog.change_color('pink')

print(dog1.color, dog2.color)

# This is a test message