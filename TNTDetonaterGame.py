import random
tntnum = random.randrange(8, 30)
p1input = 0
p2input = 0
sum = 0
player = 1
print("******")
print("* TNT *")
print("******")
print("Loading...")
print("TNT Deployed!")
while sum <= tntnum:
    if player == 1:
        print("Number: " + str(sum))
        while not(int(p1input) == 1 or int(p1input) == 3 or int(p1input) == 2):
            p1input = input("Player 1, Input the number you want to add(Only 1, 2 or 3): ")
        sum = sum + int(p1input)
        p1input = 0
        if sum >= tntnum:
            print("******")
            print("* TNT " + str(tntnum) + " *")
            print("******")
            print("EXPLODED! YOU LOSE!")
        elif sum + 6 >= tntnum:
            print("Beware! The TNT Countdown is dropping fast!")
        player = 2
    elif player == 2:
        print("Number: " + str(sum))
        while not(int(p2input) == 1 or int(p2input) == 3 or int(p2input) == 2):
            p2input = input("Player 2, Input the number you want to add(Only 1, 2 or 3): ")
        sum = sum + int(p2input)
        p2input = 0
        if sum >= tntnum:
            print("******")
            print("* TNT " + str(tntnum) + " *")
            print("******")
            print("EXPLODED! YOU LOSE!")
        elif sum + 6 >= tntnum:
            print("Beware! The TNT Countdown is dropping fast!")
        player = 1




