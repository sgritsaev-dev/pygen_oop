class PhoneNumber:
    def __init__(self, number:str) -> None:
        self.phone_number = number.replace(' ', '')
        
    def __repr__(self) -> str:
        return f"PhoneNumber('{self.phone_number}')"
    
    def __str__(self) -> str:
        return f'({self.phone_number[0:3]}) {self.phone_number[3:6]}-{self.phone_number[6:10]}'
        