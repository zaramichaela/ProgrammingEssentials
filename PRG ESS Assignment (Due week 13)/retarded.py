num = 0
i = 1
info = ["model_name", "screen_size", "cost", "brand", "processor", "os", "ram", "istorage", "quantity"]
holder = ["Samsung Galaxy Tab S 10.5", "10.50-inch", 178.99, "Samsung","Exynos 5 Octa","Android‎ ‎4.4.2" "KitKat","3GB","16GB", 20]
stocks = {1: holder}
while True:
    print("Welcome to Zara's shop, here are your options:")
    print("1. Add a new shipment")
    print("2. Current shipment(s)")
    print("3. Sell Tablet(s)")
    print("0. Exit program")
    try:
    num = int(input("What would you like to do?"))
    except ValueError:
        print("Please enter a number instead. try again.")
    if num < 0 or num > 3:
        print("Whoops! That's not a feature the store has! Try again.")
        continue
    elif num == 0:
        print("Have a nice day!")
        break
    elif num == 1:
        code = 0
        while True:
            try:
                code = int(input("Enter sales code:"))
                if(code <= 0):
                    print("The code cannot be 0 or under, try again")
                    continue
                slot = stocks.get(code,"not found")
                if slot != "not found":
                    print("Sales Code has already been taken, try again")
                    continue
                break
            except ValueError:
                print("the sales code should be an number, try again")
        isbn = input("Enter model name of tablet:")
        screen_size = input("What is the screen size? ")
        cost = 0
        while True:
            try:
                cost = float(input("What is the cost?"))
                if(cost <= 0):
                    print("The cost cannot be 0 or under, try again")
                    continue
                break
            except ValueError:
                print("The cost is not a number, try again")
        brand = input("What is the brand? ")
        processor = input("what is the processor of this tablet? ")
        os = input("What is the operating system?")
        ram = input("How much RAM does the tablet have? ")
        istorage = input("How much internal storage does the tablet have?")
        quantity  = 0
        while True:
            try:
                quantity = int(input("How many stocks do you have?"))
                if(quantity <= 0):
                    print("The stocks cannot be 0 or under, try again")
                    continue
                break
            except ValueError:
                print("The stocks is not a number, try again")
        newholder = []
        newholder.append(isbn)
        newholder.append(screen_size)
        newholder.append(cost)
        newholder.append(brand)
        newholder.append(processor)
        newholder.append(os)
        newholder.append(ram)
        newholder.append(istorage)
        newholder.append(quantity)
        stocks[code] = newholder
    elif num == 2:
        for i in stocks:
            j = 0
            print("Tablet ", i ,": ")
            for value in stocks[i]:
                print(info[j],":" ,value)
                j += 1
            print("")
            print("")

    elif num == 3:
        for key in stocks:
            print(key,":",stocks[key])
        quest = input("Select Category to sell(if neither, press Q/q):")
        if quest.lower() == "q":
            continue
        while True:
            try:
                itemfound = int(quest)
                break
            except ValueError:
                print("Please enter a number")
        item = stocks.get(itemfound,"not found")
        if item == "not found":
            print("Item is not found, please try again.")
            continue
        else:
            print("The item you have selected is : " , item)
            sellnum = 0
            while True:
                try:
                    sellnum = int(input("How many are you selling?"))
                except ValueError:
                    print("you did not enter an number. try again")
                    continue
                if(item[8] < sellnum):
                    print("Not enough stocks, please purchase within stock amount")
                    continue
                elif (sellnum <= 0):
                    print("you have entered a negative or zero number. try again")
                    continue
                else:
                    break
            stocks[itemfound][8] =stocks[itemfound][8]-sellnum
            saleprice = stocks[itemfound][2] * sellnum
            print( sellnum , "number of" , stocks[itemfound][0] , "have been sold for the total price of " , saleprice)
            ask = input("Do you wish to continue?(Y,q)")
            if(ask.lower() == "q"):
                print("Thank you")
                break
            else:
                continue
