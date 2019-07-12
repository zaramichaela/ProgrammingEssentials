# Admin Number: 194123U
# Author: Zara Teo Xiao Xuan
# PEM: CS1902
def question():
    listdata = []
    while True:
        start = input("Press enter to start or q/Q to quit.")
        if start.lower() == 'q':
            return
        model_name = input("What is the model name? ")
        if model_name.lower() == 'q':
            return
        screen_size = input("What is the screen size? ")
        if screen_size.lower() == 'q':
            return
        while True:
            cost = input("What is the cost? ")
            if cost.lower() == 'q':
                return
            try:
                cost = float(cost)
            except ValueError:
                print("You have entered an invalid cost.")
                continue
            else:
                break

        brand = input("What is the brand? ")
        if brand.lower() == 'q':
            return
        while True:
            processor = input("How many processors does this tablet have? ")
            if processor.lower() == 'q':
                return
            try:
                processor = int(processor)
            except ValueError:
                print("You have entered an invalid number of processors.")
                continue
            else:
                break
        frontcam = input("What are the specifications of the front-facing camera? ")
        if frontcam.lower() == 'q':
            return
        rearcam = input("What are the specifications of the rear facing camera? ")
        if rearcam.lower() == 'q':
            return
        display = input("What is the specifications of the display of the tablet? ")
        if display.lower() == 'q':
            return
        os = input("What is the operating system?")
        if os.lower() == 'q':
            return
        i_storage = input("How much internal storage does the tablet have?")
        if i_storage.lower() == 'q':
            return
        while True:
            ram = input("How much RAM does the tablet have? ")
            if ram.lower() == 'q':
                return
            try:
                ram = float(ram)
            except ValueError:
                print("You have entered an invalid amount of RAM")
                continue
            else:
                break

        specification = {
            "model_name": model_name,
            "screen_size": screen_size,
            "brand": brand,
            "processor": processor,

            "os": os,
            "ram": ram,
            "i_storage": i_storage
        }
        listdata.append(specification)
        print("%s has a screen size of %s and costs $%.2f." % (model_name, screen_size, cost))
        print("The brand is %s and it has %d processors. " % (brand, processor))
        print("It is running on %s OS, has %s RAM and has %s internal storage." % (os, ram, i_storage))

question()
