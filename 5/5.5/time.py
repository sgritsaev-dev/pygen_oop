class Time:
    def __init__(self, hours, minutes) -> None:
        while minutes >= 60:
            minutes-=60
            hours += 1
        self.minutes = minutes
        while hours >= 24:
            hours-=24
        self.hours = hours

    def __repr__(self):
        return f'{self.hours:02}:{self.minutes:02}'

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.__class__(self.hours+other.hours,
                                  self.minutes+other.minutes)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, self.__class__):
            self.hours += other.hours
            self.minutes += other.minutes
            while self.minutes>=60:
                self.minutes-=60
                self.hours+=1
            while self.hours>=24:
                self.hours-=24
            return self
        return NotImplemented


t = Time(22, 0)
t += Time(3, 0)
print(t)

# TEST_9:
t1 = Time(15, 50)
t2 = Time(2, 20)
print(t1 + t2)

t1 += Time(2, 20)
print(t1)
