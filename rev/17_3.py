while True:

    number = input("Enter your credit card number :")

    if number.isdigit():

        last = number[-4:]

        if len(number) == 16 and number.startswith("4"):
            validity = "valid Visa"
            print("You have a valid %s and the last 4 digit is %s" % (validity, last))

        elif len(number) == 15 and (number.startswith("34") or number.startswith("37")):
            validity = "valid Amex"
            print("You have a valid %s and the last 4 digit is %s" % (validity, last))

        else:
            if len(number) == 15:
                validity = "invalid Amex"

            elif len(number) == 16:
                validity = "invalid Visa"

            else:
                validity = "invalid credit card"

            print("You have entered an %s card numbers" % validity)
    else:
        print("Please enter digits only.")
