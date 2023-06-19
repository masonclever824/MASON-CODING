coinamount = "0"
totalamount = 0
itemone = "a. Apple Juice ~ $"
itemoneamount = 7
itemtwo = "b. Chocolate ~ $"
itemtwoamount = 12
itemthree = "c. Jagabee Fries Jumbo Pack ~ $"
itemthreeamount = 17
print("Welcome to the Intelligent Selling Machine!")
print("We are selling: ")
print(itemone + str(itemoneamount))
print(itemtwo + str(itemtwoamount))
print(itemthree + str(itemthreeamount))
while coinamount.isnumeric():
    coinamount = input("Insert Coin or Select Item: ")
    while coinamount.isnumeric() and not(coinamount=="1" or coinamount=="2" or coinamount=="5" or coinamount=="10" or coinamount=="0.1" or  coinamount=="0.2" or coinamount == "0.5"):
        coinamount = input("Invalid Coin Amount. (According to Hong Kong Coins) Please Try Again. Insert Coin: ")
    if coinamount.isnumeric():
        totalamount = totalamount + int(coinamount)
        print("Slotted In $" + str(totalamount))
        if totalamount < itemoneamount:
            print("No Available Items")
        if totalamount >= itemoneamount:
            print(itemone + str(itemoneamount))
        if totalamount >= itemtwoamount:
            print(itemtwo + str(itemtwoamount))
        if totalamount >= itemthreeamount:
            print(itemthree + str(itemthreeamount))
    else:
        if coinamount == "a":
            print("Thank You! The Apple Juice is ready!")
        elif coinamount == "b":
            print("Thank You! The Chocolate is ready!")
        elif coinamount == "c":
            print("Thank You! The Jagabee Fries Jumbo Pack is ready!")
