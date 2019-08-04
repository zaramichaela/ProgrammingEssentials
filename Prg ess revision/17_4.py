censored = []

for i in range(3):
    word = input("Enter the word to be censored: ")
    censored.append(word)

count = 0
while True:
    newstr = ""
    str = input("Enter a string : ")
    split = str.split(" ")
    finalprint = []
    for word in split:
        appended = False
        for j in censored:
            if word == j:
                count += 1
                new = word[0:1] + "*" * (len(word)-1)
                print("You have been censored %d times" % count)
                appended = True
                finalprint.append(new)
        if( not appended):
            finalprint.append(word)
    print(" ".join(finalprint))
    if count >= 3:
        print("You have been banned!")
        break
