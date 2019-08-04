num_record = int(input("No of expense records you want to enter: "))
total_amt = 0
for i in range(num_record):
    amt = float(input("Please enter the expenses amount: "))
    total_amt += amt
    i += 1
print("Total expenses you have entered is $%.2f" % total_amt)
