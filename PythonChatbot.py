def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines." )
    print("3. To determine the execution time of a program. ")
    print("4. To interrupt the execution of a program.")
    answer = int(input("Please type in the correct statement: "))
    if answer != 2:
        print("Please try again!")
    else:
        print('Completed, have a nice day!')
botname = "CleverBot2000"
print("Hello, Humans! My name is " + botname)
print("I was created by Mason using Python in 2022. ")
print("Master, I need your name to access your data and help you. Please enter your name.")
name = input("Your Name: ")
print("What a great name you have, " + name)
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105
print("Your age is " + str(age) + "! that's a good time to start programming!")
print("Now I will prove to you that I can count to any number you want.")
numbercount = int(input())
c = 0
for i in range(numbercount+1):
    print(str(c) + " !")
    c = c+1
print("I did a good job, right?")
test()