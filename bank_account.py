class BankAccount:
    def __init__(self):
        self.balance = 0
        self.overdraft_fees=0
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        net_balance=self.balance-amount-self.overdraft_fees
        self.balance-=amount if net_balance>=-100 else 0
        return self.balance
    def accumulate_interest(self, interest):
        self.balance= self.balance +self.balance*interest
        accu_int_amount=self.balance*interest
        return (self.balance,accu_int_amount)
class ChildrensAccount(BankAccount):
    def __init__(self):
        super().__init__()
    def accumulate_interest(self, amount):
        amount=10
        self.balance+= amount
        # return self.balance
        print(f"Child's account has ${childs_account.balance}")
class OverdraftAccount(BankAccount):
    def __init__(self):
        super().__init__()  
    def withdraw(self, amount):
        overdraft_penalty=40
        self.balance-=amount if self.balance<0 else overdraft_penalty

        return self.balance     

basic_account = BankAccount()
basic_account.deposit(600)
basic_account.withdraw(17)
basic_account.accumulate_interest(0.02)
childs_account = ChildrensAccount()
childs_account.deposit(34)
childs_account.withdraw(17)
childs_account.accumulate_interest(0.02)
overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
overdraft_account.withdraw(17)