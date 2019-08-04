"""method 1 part a"""
numbers = []
i = 0
for i in range(10):
    num = int(input('Enter your number %d:'%(i+1)))
    # add num into list
    numbers.append(num)
    i += 1
print(numbers)
"""
#method 2

for a in numbers:
    print(a , end =' ')

print()


#method 3
i = 0
while i < len(numbers):
    print(numbers[i])
    i = i + 1
"""
print('all items in list',numbers)
print('total items in list',len(numbers))
print('min number in list',min(numbers))
print('max number in list',max(numbers))
total = sum(numbers)
ave = total / len(numbers)
print('sum of all numbers in list',sum(numbers))
print('ave of all numbers in list',ave)

#part b
numbers_1 = []
count = int(input('Enter number of numbers u want in the list:'))
for i in range(count):
    numm = int(input('Enter number %d:'%(i+1)))
    numbers_1.append(numm)
print(numbers_1)
