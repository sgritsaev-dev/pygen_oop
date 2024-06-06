class RoundedInt(int):
    def __new__(cls, num, even=True):
        if even:
            num = num + num % 2
        else:
            num = num + (1 - num % 2)
        instance = super().__new__(cls, num)
        return instance


roundedint1 = RoundedInt(7)
roundedint2 = RoundedInt(7, False)

print(roundedint1 + roundedint2)
print(roundedint1 + 1)
print(roundedint2 + 1)

print(type(roundedint1))
print(type(roundedint2))
