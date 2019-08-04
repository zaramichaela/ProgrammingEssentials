i = 0
total = 0

number = int(input("No of expenses occurred in this month: "))

for i in range(number):
    amt = float(input("Please enter the expenses amount: "))
    i += 1
    total += amt

avg = total / number
print("Average spending of this month is $%.2f" % avg )
