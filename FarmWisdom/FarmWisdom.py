balance = 1000
'''
print(balance)

class Animal(object):
	pass
    #health
    #units
    #cost
    
class FlockOfChickens(Animal):
    #name
    #cost = $3 for chicks, $25 for pullets
    #yield = 250 eggs per bird per year, 5 layers, 1000 eggs, which you sell for $5 per dozen, so $415 per year
    def buy(self):
        #subtract cost from balance
        print("Chickens cost $15 for a flock")
        #balance = balance - 15
        #print(balance)
        assets.append("flock_of_chickens")
        #yeild
        print("A flock of chickens earns you $415 per year in egg sales.")
        balance =+ 415
        
 

assets = []

print(f"Year 0\nStarting bank balance:${balance}\nAssets:{assets}")
print(f"What do you want to do? \nOptions:\n*Buy chickens")
decision = input(">>>")
if decision == "Buy chickens":
    flock1 = FlockOfChickens()
    flock1.buy()
print(f"Ending bank balance: ${balance}")

#eventually need to do a while loop to advance the years
'''