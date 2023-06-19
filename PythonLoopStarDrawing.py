print("Hello", end=" ")
print("World")
for i in range(10):
    for i in range(1+i):
        print("*", end=" ")
    for i in range(i+1):
        print(" ", end=" ")
    print()
