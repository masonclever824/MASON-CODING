shoppingList = []
while True:
    inputer = input("add/remove/print?")
    if inputer == "add":
        item = input("The Item You Want To Add: ")
        shoppingList.insert(0, item)
    elif inputer == "remove":
        remove = input("The item no. you want to delete: ")
        remove = int(remove) - 1
        shoppingList.pop(remove)
    elif inputer == "print":
        print(shoppingList)