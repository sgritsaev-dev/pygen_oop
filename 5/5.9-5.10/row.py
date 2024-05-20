class Row:
    def __init__(self, **kwargs) -> None:
        for key, value in kwargs.items():
            object.__setattr__(self, key, value)

    def __setattr__(self, name: str, value) -> None:
        if name in self.__dict__:
            raise AttributeError('Изменение значения атрибута невозможно')
        raise AttributeError('Установка нового атрибута невозможна')

    def __delattr__(self, name: str) -> None:
        # if name in self.__dict__:
        #     raise AttributeError('Удаление атрибута невозможно')
        raise AttributeError('Удаление атрибута невозможно')

    def __repr__(self) -> str:
        ls = []
        for key, value in self.__dict__.items():
            if isinstance(value, str):
                ls.append(str(key)+"="+"'"+str(value)+"'")
            if isinstance(value, int):
                ls.append(str(key)+"="+str(value))
        return f'''Row({', '.join(ls)})'''

    def __eq__(self, value: object) -> bool:
        if isinstance(value, self.__class__):
            return list(self.__dict__.items()) == list(value.__dict__.items())
        return NotImplemented

    def __hash__(self) -> int:
        res = 0
        counter = 0
        for key, value in self.__dict__.items():
            counter += 1
            if counter % 2 == 1:
                res += (hash(key)+hash(value)//counter)
            else:
                res -= (hash(key)+hash(value)//counter)
        return res

# INPUT DATA:


# TEST_1:
row = Row(a='A', b='B', c='C')

print(row)
print(row.a, row.b, row.c)

# TEST_2:
row1 = Row(a=1, b=2, c=3)
row2 = Row(a=1, b=2, c=3)
row3 = Row(b=2, c=3, a=1)

print(row1 == row2)
print(hash(row1) == hash(row2))
print(row1 == row3)
print(hash(row1) == hash(row3))

# TEST_3:
row = Row(a=1, b=2, c=3)

try:
    row.d = 4
except AttributeError as e:
    print(e)

# TEST_4:
row = Row(a=1, b=2, c=3)

try:
    row.a = 10
except AttributeError as e:
    print(e)

# TEST_5:
row = Row(a=1, b=2, c=3)

try:
    del row.a
except AttributeError as e:
    print(e)

# TEST_6:
rows = {Row(a=1, b=2, c=3): 10, Row(d=4, e=5, f=6): 20}

print(rows)

# TEST_7:
row1 = Row()
rows = [Row(a=66, b=69, country='China'), Row(a=35, b=42, country='Singapore'), Row(a=93, b=71, country='Mongolia'),
        Row(a=10, b=82, country='Tajikistan'), Row(
            a=48, b=37, country='Anguilla'),
        Row(a=49, b=90, country='Argentina'), Row(
            a=83, b=13, country='Montserrat'),
        Row(a=93, b=67, country='Heard Island and McDonald Islands'), Row(
            a=47, b=36, country='Saint Martin'),
        Row(a=8, b=65, country='Samoa'), Row(a=77, b=25,
                                             country='Rwanda'), Row(a=23, b=48, country='Tuvalu'),
        Row(a=78, b=87, country='Gibraltar'), Row(
            a=99, b=59, country='Tajikistan'),
        Row(a=96, b=79, country="Cote d'Ivoire"), Row(
            a=36, b=91, country='Sri Lanka'),
        Row(a=96, b=38, country='Libyan Arab Jamahiriya'), Row(
            a=30, b=14, country='Palestinian Territory'),
        Row(a=15, b=26, country='Cambodia'), Row(
            a=71, b=86, country='Northern Mariana Islands'),
        Row(a=58, b=95, country='Mauritius'), Row(
            a=81, b=73, country='Syrian Arab Republic'),
        Row(a=17, b=61, country='Kazakhstan'), Row(
            a=42, b=60, country='French Southern Territories'),
        Row(a=68, b=69, country='Tunisia'), Row(a=70, b=76,
                                                country='Malawi'), Row(a=38, b=63, country='Tonga'),
        Row(a=36, b=45, country='Puerto Rico'), Row(a=46, b=30,
                                                    country='Burundi'), Row(a=78, b=82, country='Malta'),
        Row(a=27, b=53, country='Trinidad and Tobago'), Row(
            a=68, b=84, country='Monaco'),
        Row(a=17, b=77, country='Lesotho'), Row(a=16, b=100,
                                                country='Jamaica'), Row(a=40, b=45, country='Morocco'),
        Row(a=94, b=23, country='Bolivia'), Row(
            a=98, b=15, country='Equatorial Guinea'),
        Row(a=13, b=22, country='Ukraine'), Row(
            a=73, b=21, country='Saint Helena'),
        Row(a=58, b=35, country='Syrian Arab Republic'), Row(
            a=84, b=22, country='Djibouti'),
        Row(a=11, b=93, country='Macao'), Row(a=86, b=47,
                                              country='Anguilla'), Row(a=72, b=42, country='Guyana'),
        Row(a=18, b=31, country='Cambodia'), Row(a=30, b=31,
                                                 country='Taiwan'), Row(a=73, b=45, country='Maldives'),
        Row(a=54, b=35, country='Nauru'), Row(
            a=51, b=82, country='United States of America'),
        Row(a=77, b=96, country='Angola'), Row(a=59, b=82,
                                               country='Luxembourg'), Row(a=74, b=15, country='Venezuela'),
        Row(a=16, b=72, country='Korea'), Row(a=23, b=45,
                                              country='Mozambique'), Row(a=53, b=66, country='Swaziland'),
        Row(a=95, b=64, country='Niger'), Row(a=56, b=34, country='Myanmar'),
        Row(a=31, b=6, country='United States of America'), Row(
            a=15, b=29, country='Russian Federation'),
        Row(a=48, b=69, country='Brazil'), Row(a=59, b=17,
                                               country='Liberia'), Row(a=68, b=26, country='Canada'),
        Row(a=27, b=60, country='Liechtenstein'), Row(
            a=16, b=76, country='Belize'), Row(a=46, b=63, country='Chad'),
        Row(a=78, b=24, country='Croatia'), Row(a=99, b=14,
                                                country='Croatia'), Row(a=39, b=45, country='Burkina Faso'),
        Row(a=75, b=6, country='Latvia'), Row(a=33, b=9,
                                              country='Uganda'), Row(a=70, b=56, country='Congo'),
        Row(a=17, b=84, country='Iran'), Row(a=91, b=53, country='Bulgaria'),
        Row(a=78, b=85, country='Bosnia and Herzegovina'), Row(
            a=83, b=74, country='Mauritius'),
        Row(a=49, b=87, country='Gambia'), Row(a=13, b=57,
                                               country='Turkmenistan'), Row(a=64, b=81, country='Ghana'),
        Row(a=27, b=73, country="Cote d'Ivoire"), Row(
            a=73, b=88, country='Isle of Man'),
        Row(a=11, b=55, country='Guinea-Bissau'), Row(a=12, b=75,
                                                      country='Mayotte'), Row(a=81, b=78, country='Congo'),
        Row(a=38, b=13, country='Dominica'), Row(a=83, b=30,
                                                 country='Taiwan'), Row(a=76, b=43, country='San Marino'),
        Row(a=91, b=72, country='Kiribati'), Row(
            a=85, b=95, country='Costa Rica'),
        Row(a=11, b=40, country='Holy See (Vatican City State)'), Row(
            a=99, b=76, country='Syrian Arab Republic'),
        Row(a=70, b=70, country='San Marino'), Row(a=32, b=87,
                                                   country='Nigeria'), Row(a=33, b=5, country='Lithuania'),
        Row(a=59, b=9, country='Senegal'), Row(a=56, b=86,
                                               country='Vietnam'), Row(a=66, b=60, country='Angola'),
        Row(a=98, b=56, country='Maldives'), Row(
            a=22, b=59, country='Brunei Darussalam'),
        Row(a=98, b=57, country='Barbados'), Row(a=72, b=46, country='Djibouti')]

for row in rows:
    print(row != row1)

# TEST_8:
row = Row(a=16, b=100, country='Jamaica')
print(row.__eq__(1))
print(row.__ne__(1.1))

# TEST_9:
row1 = Row(a=1, b=2, c=3)
row2 = Row(a=3, b=2, c=1)
print(row1 == row2)

# TEST_10:
row1 = Row(a=1, b=2, c=3)
row2 = Row(b=1, a=2, c=3)

print(row1 == row2)
print(hash(row1) == hash(row2))
