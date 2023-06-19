thisyear = int(input("Input this year's year date(eg: 2022): "))
if thisyear % 4 == 0:
    if thisyear % 100 == 0:
        if thisyear % 400 == 0:
            print("You are lucky! This is a leap year!")
        else:
            print("Bad Luck! This is not a leap year.")
    else:
        print("You are lucky! This is a leap year!")
else:
    print("Bad Luck! This is not a leap year.")