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
ARAB = {value:key for key, value in ROMAN.items()}

def arab_to_roman(num:int)->str:
    res=''
    for key in reversed(ROMAN.keys()):
        while num>=ROMAN[key]:
            res+=key
            num-=ROMAN[key]
    return res
        
print(arab_to_roman(19))