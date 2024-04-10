class HourClock:
    def __init__(self, hour) -> None:
        self.set_hour(hour)

    def get_hour(self):
        return self.hour

    def set_hour(self, new_hour):
        if new_hour not in range(1,13):
            raise ValueError('Некорректное время')
        self.hour=new_hour
    hours = property(get_hour, set_hour)