word = "adventuresome"
guesscount = 0
guess = []
for i in range(0, len(word)):
    guess.append("_")
print(' '.join(guess))
while guesscount < 10:
    playerguess = str(input("Guess a letter: "))
    for i in range(0, len(word)):
        if word[i] == playerguess:
            guess[i] = playerguess
    if playerguess not in word:
        guesscount += 1
    print(' '.join(guess))
    print("You have: " + str(10-guesscount) + " guesses left.")
    if "_" not in guess:
        print("You Win! You Lucky Genius! The word is: " + word)
        break
input()