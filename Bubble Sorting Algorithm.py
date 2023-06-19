import random
numbers = []
for i in range(1,100):
    numbers.append(random.randrange(1, 1000))
e = input("Do you want ascending or descending?")
if  e == "ascending":
    for i in numbers:
        for j in range(0, len(numbers)-1):
            if numbers[j] > numbers[j+1]:
                temp = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = temp
if e == "descending":
    for k in numbers:
        for l in range(0, len(numbers)-1):
            if numbers[l] < numbers[l+1]:
                temp = numbers[l]
                numbers[l] = numbers[l+1]
                numbers[l+1] = temp
print(numbers)
