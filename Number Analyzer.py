tm =  0
bn = 0
sn = 9
noon = 0
noen = 0
sotn = 0
aotn = 0
nobta = 0
nosta = 0
num = 10938393838383939848383
for i in str(num):
    tm = tm + 1
    if int(i) > int(bn):
        bn = i
    if int(sn) > int(i):
        sn = i
    if i == "1" or i == "3" or i == "5" or i == "7" or i == "9":
        noon = noon + 1
    if i == "0" or i == "2" or i == "4" or i == "6" or i == "8":
        noen = noen + 1
    sotn = sotn + int(i)
aotn = sotn/tm
for i in str(num):
    if int(i) > aotn:
        nobta = nobta + 1
    if int(i) < aotn:
        nosta = nosta + 1
print("Total Numbers: " + str(tm))
print("Biggest Number: " + str(bn))
print("Smallest Number: " + str(sn))
print("Numbers That Are Odd: " + str(noon))
print("Numbers That Are Even: " + str(noen))
print("Sum Of The Numbers: " + str(sotn))
print("Average Of The Numbers: " + str(aotn))
print("Numbers That Are Bigger Than The Average: " + str(nobta))
print("Numbers That Are Smaller Than The Average: " + str(nosta))
