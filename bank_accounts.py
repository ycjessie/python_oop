class BankAccount:
    def __init__(self, account_type):
        self.type = account_type
        self.balance = 0
        self.overdraft_fees=0

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        net_balance=self.balance-amount-self.overdraft_fees
        self.balance-=amount if net_balance>=-100 else 0

        if net_balance<-100:
            print("You are broke!")
        if self.balance<0 :
            self.overdraft_fees +=20
        return self.balance


checking = BankAccount('checking')
savings = BankAccount('savings')
checking.deposit(1000)
savings.deposit(400)