a = int(input("Please Input the 1st Side Length: "))
b = int(input("Please Input the 2nd Side Length: "))
c = int(input("Please Input the 3rd Side Length: "))
if a+b>c and b+c>a and a+c>b:
    if a==b and b==c:
        print("This is an Equilateral Triangle.")
    else:
        if a==b or b==c or a==c:
            if a*a+b*b==c*c or b*b+c*c==a*a or a+a+c*c==b*b:
                print("This is a Right Angle Isosceles Triangle.")
            else:
                print("This is an Isosceles Triangle.")
        else:
            if  a*a+b*b==c*c or b*b+c*c==a*a or a+a+c*c==b*b:
                print("This is a Right Angle Triangle.")
            else:
                print("This is a Scalene Triangle.")
else:
    print("It is NOT A TRIANGLE!")
