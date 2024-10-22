

class BankAccount:
    def __init__(self, iban: str, name: str, balance: float=0):
        self.iban: str = iban
        self.name: str = name
        self.balance: float = balance

    def get_balance(self):
        return (self.balance)
    
    def get_name(self):
        return(self.name)
    
    def get_iban(self):
        return(self.iban)
    
    def deposit(self, amount: float):
        if amount > 0:
            self.balance = self.balance + amount
        else: 
            raise ValueError()
        return(amount)
    
    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError()
        elif self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError()
        return(amount)
    
    def transfer(self, destination_account, amount: float):
        if amount <= 0:
            raise ValueError()
        self.withdraw(amount)
        destination_account.deposit(amount)
        return(amount)
    pass


class MinimumBalanceAccount(BankAccount):
    def __init__(self, iban: str, name: str, minimum_balance: float=100, initial_deposit: float=100):
        if minimum_balance <= 0:
            raise ValueError()
        if initial_deposit < minimum_balance:
            raise ValueError()
        super().__init__(iban, name, balance=initial_deposit)
        self.minimum_balance = minimum_balance

    def set_minimum_balance(self, amount: float):
        if amount <= 0:
            raise ValueError()
        if amount > self.balance:
            raise ValueError()
        self.minimum_balance = amount
        return(amount)
    
    def get_minimum_balance(self):
        return(self.minimum_balance)

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError()
        elif self.balance - amount >= self.minimum_balance:
            self.balance -= amount
            return amount
        else:
            raise ValueError()
    
    pass