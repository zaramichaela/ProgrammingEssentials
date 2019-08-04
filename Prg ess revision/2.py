number = []
times = int(input('How many numbers do u want to add?'))
i = 0
c = 1

while i < times:
    num = int(input('What is number %d: ' % (i + 1)))
    i = i + 1
    number.append(num)
print(number)
''' method 2

for i in range(times):
    num = int(input('number %d:'% c))
    c = c + 1
    number.append(num)
print(number)
'''
