from src.FarmWisdom.Accounting import Account
      
def buyFlockOfChickens():
    print("Chickens cost $15 for a flock")
    bank_account.buy(15)
    assets.append("flock_of_chickens")
    print("A flock of chickens earns you $415 per year in egg sales.")
    bank_account.earnings(415)
    
assets = []
bank_account = Account(1000)

print(f"Year 0\nStarting bank balance:${bank_account.balance}\nAssets:{assets}\n"
f"You buy a flock of chickens.")
buyFlockOfChickens()
print(f"\nYear 1\nStarting bank balance:${bank_account.balance}\nAssets:{assets}")


'''

print(f"What do you want to do? \nOptions:\n*Buy chickens")
decision = input(">>>")
if decision == "Buy chickens":
    flock1 = FlockOfChickens()
    flock1.buy()
print(f"Ending bank balance: ${balance}")

#eventually need to do a while loop to advance the years
'''