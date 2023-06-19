hkd_rmb = 0.86
sell = str(input("Input your Currency Used: "))
buy = str(input("Input the Currency you want to change to: "))
er = 1
finalamount = 0
if sell=="HKD" and buy=="RMB":
    er=hkd_rmb
if sell=="RMB" and buy=="HKD":
    er=1/hkd_rmb
if er == 1:
    print("We do not support this currency. Please Try Another Currency. ")
else:
    amount = int(input("Input the amount of the Currency Used: "))
    finalamount = float(amount*er)
    print(finalamount)
