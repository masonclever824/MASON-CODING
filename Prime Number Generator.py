primeNumber = []
answer = int(input("Which No. of Prime Number do you want?"))
number = 2
while len(primeNumber) != answer: 
    canBeDivided = False
    for prime in primeNumber:
        if number%prime == 0:
            canBeDivided = True
    if canBeDivided == False:
        primeNumber.append(number)
    number = number + 1
answer -= 1
number = primeNumber[answer]
print(number)