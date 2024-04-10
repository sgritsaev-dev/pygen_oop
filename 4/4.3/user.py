class User:
    def __init__(self, name, friends=0) -> None:
        self.name = name
        self.friends = friends
    
    def add_friends(self, amount):
        self.friends+=amount

user = User('Timur')

user.add_friends(2)
user.add_friends(2)
user.add_friends(3)

print(user.friends)