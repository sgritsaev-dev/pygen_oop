class Cat:
    def __init__(self, name) -> None:
        self._name = name

    @classmethod
    def class_m(cls):
        print ('class')
    
    def exemple(self):
        print('example')
    
    def shit():
        print ('shit')

cat = Cat('dog')

cat.class_m()

Cat.shit()

# Cat.exemple()

# cat.shit()

Cat.class_m()