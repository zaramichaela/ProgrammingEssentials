import datetime

num = 0
i = 1
x = datetime.datetime.now()
sale = []
info = ["model_name", "screen_size", "cost", "brand", "processor", "os", "ram", "istorage", "quantity"]
infosales = ["date", "model_name", "screen_size", "cost", "brand", "processor", "os", "ram", "istorage", "quantity"]
holder = ["Samsung Galaxy Tab S 10.5", "10.50-inch", 178.99, "Samsung","Exynos 5 Octa","Android ‎4.4.2","3GB","16GB", 20]
holder2 = ["Apple IPad Pro 11-inch ", "11-inch", 1499.99, "Apple","A12X Bionic","MAC","2GB","512GB", 30]
holder3 = ["Huawei Mediapad T3", "8-inch", 350.00, "Huawei","Qualcomm Snapdragon 425","Android ‎7.0","2GB","16GB", 20]
holder4 = ["Huawei Mediapad M5", "10.5-inch", 500.00, "Huawei","Qualcomm Snapdragon 725","Android ‎8.0","4GB","32GB", 5]
stocks = {"a1": holder,
        "a2": holder2,
        "a3": holder3,
        "a4": holder4,
        }
while True:
    print("Welcome to Zara's Tablet shop, here are your options:")
    print("1. Add a new shipment")
    print("2. Current shipment(s)")
    print("3. Create sale(s)")
    print("4. Print sales details")
    print("5. Print daily revenue select by date DD/MM/YYYY")
    print("6. Print monthly revenue select by date MM/YYYY")
    print("0. Exit program")
    while True:
        try:
            num = int(input("What would you like to do?"))
            break
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
                quest = input("Select code to sell(If neither, press Q/q):")
                if (quest.lower() == "q"):
                    break
        item = stocks.get(itemfound,"not found")
        if item == "not found":
            print("Item is not found, please try again.")
            continue
        else:
            print("The item you have selected is : " , item)
            date1 = 0
            while True:
                try:
                    day = int(input("Enter a day:"))
                    month = int(input("Enter a month:"))
                    year = int(input("Enter a year:"))
                    date = datetime.date(year, month, day)
                    break
                except ValueError:
                    print("Error, you did not enter the date correctly.")
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
    elif num == 4:
        for item in sale:
            num = 0
            for details in item:
               print(infosales[num] , ":" , details)
               num +=1
    elif num == 5:
        date1 = 0
        while True:
            try:
                day = int(input("Enter a day:"))
                month = int(input("Enter a month:"))
                year = int(input("Enter a year:"))
                date1 = datetime.date(year, month, day)
                break
            except ValueError:
                print("Error, you did not enter the date correctly.")
        totalrevenue = 0
        for item in sale:
            #you have to find all the sales that occurs on the input date
            if item[0] == date1:
                #if the date equals input date
                g = 0
                for details in item:
                    #if details is date
                    if g == 0:
                        g += 1
                        continue
                    else:
                        print(infosales[g] , ":" , details)
                    g += 1

                priceforitem = item[3]*item[9]
                print("Total price:" , priceforitem)
                print("=========="*10)
                totalrevenue += priceforitem
        print()
        print("The total revenue for", date1.strftime('%d-%m-%Y') , "is $" + str(totalrevenue))
    elif num == 6:
        date1 = 0
        date2 = 0
        while True:
            try:
                month = int(input("Enter a month:"))
                year = int(input("Enter a year:"))
                date1 = datetime.date(year, month, 1)
                nextmonth = month + 1
                if(month == 13):
                    nextmonth = 1
                    year +=1
                date2 = datetime.date(year, nextmonth, 1)
                break
            except ValueError:
                print("Error, you did not enter the date correctly.")
                traceback.print_exc()
        totalrevenue = 0
        for item in sale:
            #you have to find all the sales that occurs on the input date
            if (date1 <= item[0] < date2):
                #if the date equals inputted date
                g = 0
                for details in item:
                    #if details is date
                    if g == 0:
                        g += 1
                        continue
                    else:
                        print(infosales[g] , ":" , details)
                    g += 1
                priceforitem = item[3]*item[9]
                print("Total price:" , priceforitem)
                print("=========="*10)
                totalrevenue += priceforitem
        print()
        print("The total revenue for the month of", date1.strftime('%m-%Y') , "is $" + str(totalrevenue))




    ask = input("Do you wish to continue? Enter Q/q to quit.")
    if(ask.lower() == "q"):
        print("Thank you")
        break
    else:
        continue
