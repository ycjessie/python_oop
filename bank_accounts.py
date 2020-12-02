class BankAccount:
    def __init__(self, account_type):
        self.type = account_type
        self.balance = 0
        self.overdraft_fees=0

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if self.balance<amount:
            print("You are broke!")
        else:
            self.balance -= amount
        return self.balance


checking = BankAccount('checking')
savings = BankAccount('savings')
checking.deposit(1000)
savings.deposit(400)