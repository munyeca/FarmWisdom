class Account:
    def __init__(self, starting_balance):
        self.balance = starting_balance

    def buy(self, cost):
        self.balance -= cost
    
    def earnings(self, income):
        self.balance += income
        
