from functools import total_ordering

ROMAN = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000,
}


@total_ordering
class RomanNumeral:
    def __init__(self, number: str) -> None:
        self.number = number

    def __str__(self) -> str:
        return self.number

    @staticmethod
    def arab_to_roman(num: int) -> str:
        res = ""
        for key in reversed(ROMAN.keys()):
            while num >= ROMAN[key]:
                res += key
                num -= ROMAN[key]
        return res

    def __int__(self):
        res = 0
        numbers = list(map(lambda x: ROMAN[x], self.number))
        max_num_index = numbers.index(max(numbers))
        for i in range(len(numbers)):
            if i < max_num_index:
                res -= numbers[i]
            else:
                try:
                    if numbers[i] >= numbers[i + 1]:
                        res += numbers[i]
                    else:
                        res -= numbers[i]
                except IndexError:
                    res += numbers[i]
        return res

    def __eq__(self, value: object) -> bool:
        if isinstance(value, self.__class__):
            return int(self) == int(value)
        return NotImplemented

    def __lt__(self, value: object) -> bool:
        if isinstance(value, self.__class__):
            return int(self) < int(value)
        return NotImplemented

    def __add__(self, value):
        if isinstance(value, self.__class__):
            return self.__class__(self.arab_to_roman(int(self) + int(value)))
        return NotImplemented

    def __sub__(self, value):
        if isinstance(value, self.__class__):
            return self.__class__(self.arab_to_roman(int(self) - int(value)))
        return NotImplemented


# TEST_1:
number = RomanNumeral("IV") + RomanNumeral("VIII")

print(number)
print(int(number))

# TEST_2:
number = RomanNumeral("X") - RomanNumeral("VI")

print(number)
print(int(number))

# TEST_3:
a = RomanNumeral("X")
b = RomanNumeral("XII")

print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# TEST_4:
a = RomanNumeral("X")
b = RomanNumeral("X")

print(a == b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# TEST_5:
number = RomanNumeral("MXL") + RomanNumeral("MCDVIII") - RomanNumeral("I")

print(number)
print(int(number))

# TEST_6:
number = (
    RomanNumeral("I") + RomanNumeral("II") + RomanNumeral("III") -
    RomanNumeral("V")
)

print(number)
print(int(number))

# TEST_7:
romans1 = ["I", "X", "L", "IV", "IX", "XLV", "CXXIV", "MCMXCIV"]
romans2 = ["I", "V", "L", "VI", "XI", "XXV", "CDXLVIII", "MCMXCI"]

for x, y in zip(romans1, romans2):
    number = RomanNumeral(x) + RomanNumeral(y)
    print(number, int(number))

# TEST_8:
romans1 = ["III", "X", "L", "C", "M", "XXV", "XC", "MMMCMXXXV"]
romans2 = ["II", "V", "X", "L", "D", "IV", "VIII", "MCMXCIV"]

for x, y in zip(romans1, romans2):
    number = RomanNumeral(x) - RomanNumeral(y)
    print(number, int(number))

# TEST_9:
romans = ["I", "IV", "IX", "XII", "XXV", "XLV", "LXIX", "XC", "CDXLVIII"]

for num in romans:
    print(RomanNumeral(num), int(RomanNumeral(num)))

# TEST_10:
roman = RomanNumeral("L")
print(roman.__eq__(1))
print(roman.__ne__(1.1))
print(roman.__gt__(range(5)))
print(roman.__lt__([1, 2, 3]))
print(roman.__ge__({4, 5, 6}))
print(roman.__le__({1: "one"}))
