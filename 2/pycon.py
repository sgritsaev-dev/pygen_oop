from calendar import monthcalendar
from datetime import date


def pycon(year, month):
    counter = 0
    for week in monthcalendar(year, month):
        if week[3] != 0:
            counter += 1
        if counter == 4:
            return date.strftime(date(day=week[3], month=month, year=year), "%d.%m.%Y")


year = int(input())
month = int(input())
print(pycon(year, month))
