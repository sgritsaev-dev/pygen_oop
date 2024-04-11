class Pet:
    list_o_pets=[]

    def __init__(self, name) -> None:
        self.name = name
        __class__.list_o_pets.append(self)

    @classmethod
    def first_pet(cls):
        try:
            return cls.list_o_pets[0]
        except:
            return None

    @classmethod
    def last_pet(cls):
        try:
            return cls.list_o_pets[-1]
        except:
            return None

    @classmethod
    def num_of_pets(cls):
        return len(cls.list_o_pets)
    
pet1 = Pet('Ratchet')
pet2 = Pet('Clank')
pet3 = Pet('Rivet')

print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets())