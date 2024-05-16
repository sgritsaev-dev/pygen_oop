from datetime import date


class DateFormatter:
    def __init__(self, country_code) -> None:
        self.country_code = country_code
        self.variants = {
            "ru": "%d.%m.%Y",
            "us": "%m-%d-%Y",
            "ca": "%Y-%m-%d",
            "br": "%d/%m/%Y",
            "fr": "%d.%m.%Y",
            "pt": "%d-%m-%Y",
        }

    def __call__(self, d: date):
        return date.strftime(d, self.variants[self.country_code])
