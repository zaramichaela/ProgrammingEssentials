# Admin Number: 194123U
# Author: Zara Teo Xiao Xuan
# PEM: CS1902
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

print("%s has a screen size of %s and costs $%.2f. " % (model_name, screen_size, cost))
print("The brand is %s and it has %d processors. " % (brand, processor))
print("It is running on %s OS, has %s RAM and has %s internal storage." % (os, ram, i_storage))
