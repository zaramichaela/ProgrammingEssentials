num = 0
i = 1
import datetime
x = datetime.datetime.now()
sale = []
info = ["model_name", "screen_size", "cost", "brand", "processor", "os", "ram", "istorage", "quantity"]
holder = ["Samsung Galaxy Tab S 10.5", "10.50-inch", 178.99, "Samsung","Exynos 5 Octa","Android‎ ‎4.4.2" "KitKat","3GB","16GB", 20]
stocks = {1: holder}
while True:
    print("Welcome to Zara's Tablet shop, here are your options:")
    print("1. Add a new shipment")
    print("2. Current shipment(s)")
    print("3. Create sale(s)")
    print("4. Print sales details")
    print("5. Print daily revenue select by date DD/MM/YYYY")
    print("6. Print monthly revenue select by date MM/YYYY")
    print("0. Exit program")
    try:
        num = int(input("What would you like to do?"))
    except ValueError:
        print("Please enter a number instead. try again.")
    if num < 0 or num > 6:
        print("Whoops! That's not a feature that the store has! Try again.")
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
        model_name = input("Enter model name of tablet:")
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
        processor = input("What is the processor of this tablet? ")
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
        newholder.append(model_name)
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
        quest = input("Select code to sell(If neither, press Q/q):")
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
                    print("You did not enter an number. Try again")
                    continue
                if(item[8] < sellnum):
                    print("Not enough stocks, please purchase within stock amount")
                    continue
                elif (sellnum <= 0):
                    print("you have entered a negative or zero number. Try again")
                    continue
                else:
                    break
            stocks[itemfound][8] =stocks[itemfound][8]-sellnum
            saleprice = stocks[itemfound][2] * sellnum
            print( sellnum , "number of" , stocks[itemfound][0] , "have been sold for the total price of $" ,saleprice)
            date = datetime.date.today()

            solditem = [date]
            j = 0
            for details in stocks[itemfound]:
                #add all details into stocks besides quantity.
                if(j == 8):
                    solditem.append(sellnum)
                else:
                    solditem.append(details)
                j += 1
            sale.append(solditem)
    #elif num == 4:
    #    for item in sale:

    elif num == 5:
        date1 = 0
        while True:
            try:
                day = int(input('Enter a day'))
                month = int(input('Enter a month'))
                year = int(input('Enter a year'))
                date1 = datetime.date(year, month, day)
                break
            except ValueError:
                print("Error, you did not enter the date correctly.")
        inputdaysales = []
        print (sale)
        for item in sale:
            #you have to find all the sales that occurs on the input date
            if item[0] == date1:
                inputdaysales.append(item)
        totalrevenue = 0
        for item in inputdaysales:
            g = 0
            for sales in item:
                if g == 0:
                    continue
                print(info[g] , ":" , sales)
                g += 1
            
            priceforitem = item[3]*item[8]
            print("Total price:" , item[3]*item[8])
            totalrevenue += priceforitem
        print()
        print("The total revenue for", date1.strftime('%d-%m-%Y') , "is $" + str(totalrevenue))
    elif num == 6:
        month = int(input('Enter a month'))
        year = int(input('Enter a year'))
        date2 = datetime.date(day, month, year)

    ask = input("Do you wish to continue? Enter Q/q to quit.")
    if(ask.lower() == "q"):
        print("Thank you")
        break
    else:
        continue
