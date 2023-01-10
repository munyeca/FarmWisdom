from src.FarmWisdom.Accounting import Account
      
def buyFlockOfChickens():
    print("Chickens cost $15 for a flock")
    bank_account.buy(15)
    assets.append("flock_of_chickens")
    print("A flock of chickens earns you $415 per year in egg sales.")
    bank_account.earnings(415)
    
assets = []
bank_account = Account(1000)

print(f"Year 0\nStarting bank balance:${bank_account.balance}\n"
f"Assets:{assets}\nWhat do you want to do?\nOptions:\n"
f"A. Buy chickens\nB. Fold the farm")
decision = ''
while decision not in ["A", "B"]:
    print("A or B?")
    decision = input(">>>").upper()
if decision == "A":
    print(f"You buy a flock of chickens.")
    buyFlockOfChickens()
if decision == "B":
    print("It was a good run while it lasted.")
    exit()
print(f"\nYear 1\nStarting bank balance:${bank_account.balance}\nAssets:{assets}")

#eventually need to do a while loop to advance the years
