# https://git.generalassemb.ly/prudential-0921/python-oop/blob/master/readme.md
class BankAccount:
    def __init__(self):
        self.balance = 0
        self.interest = 1.02
    #dunder method Dunder is short-hand for double underscore.
    #https://git.generalassemb.ly/prudential-0921/python-oop/blob/master/readme.md#what-are-dunder-methods-magic-methods
    def __str__(self):
        return f"Current Balance: $ {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        net_balance = self.balance-amount
        self.balance -= amount if net_balance >= -100 else 0
        return self.balance

    def accumulate_interest(self):
        self.balance *= self.interest
        return self.balance

#ChildrensAccount class inherits from BankAccount
class ChildrensAccount(BankAccount):
    def __init__(self):
        super().__init__()
        #ChildrensAccount has no interest rate
        self.interest_rate=0.0
    # accumulate_interest method
    def accumulate_interest(self):
        self.balance += 10
        return self.balance
        


class OverdraftAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.interest_rate=0.0
        #an overdraft_penalty property that defaults to $40.
        self.overdraft_penalty = 40
    
    def withdraw(self, amount):
        if amount>self.balance:
            self.balance -= self.overdraft_penalty
            return False
        else: return super().withdraw(amount)
    def accumulate_interest(self):
        if self.balance<=0:
                return self.balance 
        #force to reference Parent class
        else:return super().accumulate_interest()

basic_account = BankAccount()
basic_account.deposit(600)
print(f"Basic account has ${basic_account.balance}")
basic_account.withdraw(17)
print(f"Basic account has ${basic_account.balance}")
basic_account.accumulate_interest()
print(f"Basic account has ${basic_account.balance}")
childs_account = ChildrensAccount()
childs_account.deposit(34)
print(f"Child's account has ${childs_account.balance}")
childs_account.withdraw(17)
print(f"Child's account has ${childs_account.balance}")
childs_account.accumulate_interest()
print(f"Child's account has ${childs_account.balance}")
overdraft_account = OverdraftAccount()
overdraft_account.deposit(12)
overdraft_account.withdraw(17)
print(f"Overdraft account has ${overdraft_account.balance}")
overdraft_account.accumulate_interest()
print(f"Overdraft account has ${overdraft_account.balance}")
