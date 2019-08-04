import random
hidden_numbers = []
tries = 0

for i in range(4):
    hidden_numbers.append(random.randint(0,9))

print('Lucky numbers', hidden_numbers)
count =0
while True:
    guess = input("Guess the 4 numbers in as few tries: ")
    if guess.isdigit():
        for g in guess:
            for j in hidden_numbers:
                if j == int(g):
                    count += 1
                    break
        if count == 4:
            print("All correct")
            break
        else:
            print("*" * count)
            count = 0
    else:
        print("THIS IS NOT A NUMBER U DUMBASS")

if guess == hidden_numbers:
    print("Yes! You got it with %d tries!"  )
