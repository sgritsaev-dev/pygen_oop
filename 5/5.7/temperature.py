class Temperature:
    def __init__(self, temperature) -> None:
        self.temperature = temperature

    def __str__(self):
        return f"{float(self.temperature)}°C"

    def to_fahrenheit(self):
        return (self.temperature * 9 / 5) + 32

    @staticmethod
    def from_fahrenheit(temperature_f):
        return Temperature(round((temperature_f - 32) * 5 / 9, 2))

    def __bool__(self):
        return self.temperature > 0

    def __int__(self):
        return int(self.temperature)

    def __float__(self):
        return float(self.temperature)


t = Temperature.from_fahrenheit(41)

print(t)
print(int(t))
print(float(t))
print(t.to_fahrenheit())

t = Temperature.from_fahrenheit(132.7)
print(t)
