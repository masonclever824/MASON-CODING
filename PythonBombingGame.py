import random
bombnumber = random.randrange(100)
guess = 0
player = 1
mininum = 1
maximum = 100
while bombnumber != guess:
    guess = int(input("Player " + str(player) + " Guess: "))
    if  maximum > guess > bombnumber:
        maximum = guess
        print(str(mininum) + "-" + str(maximum))
    if mininum < guess < bombnumber:
        mininum = guess
        print(str(mininum) + "-" + str(maximum))
    if player == 2:
        player = 1
    else:
        player = 2
print("DIEEEEEEE! BECAUSE YOU GET BOMBED!")