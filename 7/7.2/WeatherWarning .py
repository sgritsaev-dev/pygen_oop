from datetime import date


class WeatherWarning:
    def rain(self):
        print("Ожидаются сильные дожди и ливни с грозой")

    def snow(self):
        print("Ожидается снег и усиление ветра")

    def low_temperature(self):
        print("Ожидается сильное понижение температуры")


class WeatherWarningWithDate(WeatherWarning):
    def rain(self, dt: date):
        print(date.strftime(dt, "%d.%m.%Y"))
        super().rain()

    def snow(self, dt: date):
        print(date.strftime(dt, "%d.%m.%Y"))
        super().snow()

    def low_temperature(self, dt: date):
        print(date.strftime(dt, "%d.%m.%Y"))
        super().low_temperature()
