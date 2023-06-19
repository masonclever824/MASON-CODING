a=0
b=1
for i in range(10):
    answer=a+b
    if i==9:
        print(answer, end=" ")
    a=b
    b=answer
