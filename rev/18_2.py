sentence = input("Enter a sentence: ")
letter = input("Enter a letter: ")

no_of_char = len(sentence)
last_occ = sentence.rfind(letter)

letters = 0
digit = 0
other = 0

for i in sentence:
    if i.isalpha():
        letters+=1
    elif i.isnumeric():
        digit+=1
    else:
        other+=1

remainder = sentence[last_occ:]
print("This sentence has %d characters" % no_of_char)
print("There are %d digit(s), %d letter(s) and %d other(s)." % (digit, letters, other))
print("The last occurence of %s is at index %s" % (letter, last_occ))
print(remainder)
