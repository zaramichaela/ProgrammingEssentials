num = 0
i = 1
info = [model_name, screen_size, cost, brand, processor, os, ram, istorage]
holder = ["Samsung Galaxy Tab S 10.5", "10.50-inch", "$178.99", "Samsung","Exynos 5 Octa"," Android‎ ‎4.4.2 "KitKat"‎","3GB","16GB"]
while True:
    print("Welcome to Zara's shop, here are your options:")
    print("1. Add a new shipment")
    print("2. Current shipment(s)")
    print("3. Available Stocks")
    print("0. Exit program")
    num = int(input("What would you like to do?"))
if num < 0 or num > 3:
    print("Whoops! That's not a feature the store has! Try again.")
    continue
if num == 0:
    print("Have a nice day!")
    break
if num == 1:
    isbn = input("Enter model name of tablet:")
    code = int(input("Enter sales code:"))
    slot = stocks.get("%d" %code,"not found")
    if slot != "not found":
        print("Sales Code has already been taken")
        number = int(input("Enter sales code:"))
    elif number <= 0:
        print("Sales code has to be more than zero")
        number = int(input("Enter sales code:"))
    screen_size = input("What is the screen size? ")
    cost = float(input("What is the cost?"))
    brand = input("What is the brand? ")
    processor = float(input("How many processors does this tablet have? "))
    os = input("What is the operating system?")
    ram = input("How much RAM does the tablet have? ")
    istorage = input("How much internal storage does the tablet have?")
