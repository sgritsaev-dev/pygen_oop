import re

class CaseHelper:
    @staticmethod
    def is_snake(text:str) -> bool:
        if re.fullmatch(r"\b([a-z]{1,}_{0,1}[a-z]{1,}){1,}\b", text):
            return True
        return False
    
    @staticmethod
    def is_upper_camel(text:str) -> bool:
        if re.fullmatch(r"\b([A-Z]{1}[a-z]{1,}){1,}\b", text):
            return True
        return False
    
    @staticmethod
    def to_snake(text:str) -> str:
        string=''
        for char in text:
            if char.islower():
                string = string+''.join(char)
            else:
                string = string+''.join('_'+char.lower())
        return string.strip('_')
    
    @staticmethod
    def to_upper_camel(text:str) -> str:
        string = ''.join(el.capitalize() for el in text.split('_'))
        return string
    
print(CaseHelper.to_upper_camel('beegeek'))
print(CaseHelper.to_upper_camel('bee_geek'))
print(CaseHelper.to_snake('Beegeek'))
print(CaseHelper.to_snake('BeeGeek'))
    