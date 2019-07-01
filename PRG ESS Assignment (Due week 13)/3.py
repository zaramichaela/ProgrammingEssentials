specifications = {}

def add_new_item():
    while True:
        exists = False
        while not exists:
            code = input("What is the new item code (must be unique):")
            for key in specifications:
                if(code == key):
                    exists = True
                    print("The item code exists, please enter another item code.")
        model_name = input("What is the model name? ")
        screen_size = input("What is the screen size? ")
        cost = input("What is the cost? ")
        while True:
            try:
                cost = float(cost)
                break
            except ValueError:
                print("You have entered an invalid cost.")
                cost = input("What is the cost? ")
        brand = input("What is the brand? ")
        processor = input("How many processors does this tablet have? ")
        while True:
            try:
                processor = int(processor)
                break
            except ValueError:
                print("You have entered an invalid number of processors.")
                processor = input("How many processors does this tablet have? ")

        os = input("What is the operating system?")
        ram = input("How much RAM does the tablet have? ")
        while True:
            try:
                ram = float(ram)
                break
            except ValueError:
                print("You have entered an invalid amount of RAM")
                ram = input("How much RAM does the tablet have? ")

        i_storage = input("How much internal storage does the tablet have?")

        currentspec = {
            "model_name": model_name,
            "screen_size": screen_size,
            "cost": cost,
            "brand": brand,
            "processor": processor,
            "os": os,
            "ram": ram,
            "i_storage": i_storage
        }

        specifications[code] = currentspec
        print("%s has a screen size of %s and costs $%.2f. " % (model_name, screen_size, cost))
        print("The brand is %s and it has %d processors. " % (brand, processor))
        print("It is running on %s OS, has %s RAM and has %s internal storage." % (os, ram, i_storage))

        leave = input("Do you want to quit the program? Enter q or Q to quit.")

        if leave.lower() == "q":
            break

        code += 1


def addsales():
    code = input("Enter item code of tablet:")
    exist = False
    while not exist:
        for key in specifications:
            if(key == code):
                exist = True
        print("please enter a valid tablet item code")
    tablet = specifications[code]
    while True:
        quantity = input("enter the quantity of the purchase:")
        try:
            int(quantity)
            break
        except ValueError:
            print("enter a integer number")
    receipt = input("enter receipt number:")
    sales[receipt] = {
     "tablet_code" : code,
     "quantity" : quantity,
     "total_price" : (specifications[code])["cost"] * quantity
    }







