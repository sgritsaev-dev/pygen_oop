class Money:
    def __init__(self, amount) -> None:
        self.amount = amount
        
    def __repr__(self) -> str:
        return f'{self.amount} руб.'
    
    def __pos__(self):
        return Money(abs(self.amount))
    
    def __neg__(self):
        return Money(-abs(self.amount))
    
    
    
money = Money(-100)

print(money)
print(+money)
print(-money)