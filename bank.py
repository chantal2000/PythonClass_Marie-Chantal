class Account:
    def __init__(self,name,phonenumber,loan):
        self.name=name
        self.loan=loan
        self.phonenumber=phonenumber
        self.balance=0
    def showbalance(self):
        return  f"Hello {self.name} your balance is {self.balance}"
    def deposit(self,amount):
        self.balance += amount
        if amount<0:
            return f"amount can't be less than 0"
        else:
            return self.showbalance()
    def withdraw(self,amount):
        self.balance-=amount
        if amount>self.balance:
            return f"Your balance is {self.balance} and You can not withdraw {amount}"
        else:
            return self.showbalance()
    def borrow(self,amount):
        return f"Hello {self.name}, you have borrowed{self.loan}; your new balance is {amount-self.loan} "
    def repayloan(self,amount):
        return f"Hello {self.name}, you have repaid {self.loan} ; your new balance is{amount-self.loan+self.loan}"

    
