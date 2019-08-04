price = float(input("Enter the list price $"))
if price < 10 :
    margin = 0.05

if price >= 10 and price <= 50:
    margin = 0.08

if price > 50:
    margin = 0.1

if price < 0 :
    print("End of the Program !")
    exit()
    
retail = price + (price * margin)
print("The Retail Price for product $%.2f with margin %.2f is $%.2f" % (price, margin, retail))
