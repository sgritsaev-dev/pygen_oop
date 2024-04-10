class BankAccount:
    def __init__(self, balance=0) -> None:
        self._balance=balance
    
    def get_balance(self):
        return self._balance
    
    def deposit(self, amount):
        self._balance+=amount

    def withdraw(self, amount):
        if self._balance>=amount:
            self._balance-=amount
        else:
            raise ValueError('На счете недостаточно средств')
    
    def transfer(self, account, amount):
        if self._balance>=amount:
            self._balance-=amount
            account._balance+=amount
        else:
            raise ValueError('На счете недостаточно средств')

