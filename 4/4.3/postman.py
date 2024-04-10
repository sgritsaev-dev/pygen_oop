class Postman:
    def __init__(self) -> None:
        self.delivery_data = list()

    def add_delivery(self, st, bld, appt):
        self.delivery_data.append(tuple([st, bld, appt]))

    def get_houses_for_street(self, street):
        res = []
        for el in self.delivery_data:
            if el[0]==street and el[1] not in res:
                res.append(el[1])
        return res

    def get_flats_for_house(self, street, house):
        res = []
        for el in self.delivery_data:
            if (el[0]==street and el[1]==house) and el[2] not in res:
                res.append(el[2])
        return res