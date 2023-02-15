from src.FarmWisdom.Accounting import Account

years_count = []
assets = []
bank_account = Account(1000)

def goodRun():
    raise SystemExit()

class year():
    def next():
        print(f"\n========================================\n"
        f"Year {len(years_count)}\nBank balance:${bank_account.balance}\n"
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
            goodRun()
        years_count.append(1)
        fatherTime(year)
        
def fatherTime(the_year):
    progress = the_year.next()

def buyFlockOfChickens():
    print("Chickens cost $15 for a flock")
    bank_account.buy(15)
    assets.append("flock_of_chickens")
    print("A flock of chickens earns you $415 per year in egg sales.")
    bank_account.earnings(415)