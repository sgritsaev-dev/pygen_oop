class IPAddress:
    def __init__(self,ipaddress) -> None:
        self.ipaddress = ipaddress
        
    def __repr__(self) -> str:
        if isinstance(self.ipaddress, str):
            self.ipaddress=self.ipaddress.split('.')
        return f"IPAddress('{self.ipaddress[0]}.{self.ipaddress[1]}.{self.ipaddress[2]}.{self.ipaddress[3]}')"
    
    def __str__(self) -> str:
        if isinstance(self.ipaddress, str):
            return self.ipaddress
        else:
            return f'{self.ipaddress[0]}.{self.ipaddress[1]}.{self.ipaddress[2]}.{self.ipaddress[3]}'
        
ip = IPAddress([1, 1, 10, 10])

print(str(ip))
print(repr(ip))