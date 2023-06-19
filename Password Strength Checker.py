strength = 0
remark = ''
nolc = 0
nouc = 0
nod = 0
now = 0
nosc = 0
print("===== Welcome to the Password Strength Checker 2000! =====")
password = input("Please Enter the Password: ")
for char in list(password):
    if char.islower():
        nolc = nolc + 1
    elif char.isupper():
        nouc = nouc + 1
    elif char.isnumeric():
        nod = nod + 1
    elif char == " ":
        now = now + 1
    else:
        nosc = nosc + 1
if nolc >= 1:
    strength = strength + 1
if nouc >= 1:
    strength = strength + 1
if nod >= 1:
    strength = strength + 1
if now >= 1:
    strength = strength + 1
if nosc >= 1:
    strength = strength + 1
if strength == 1:
    remark = "Remarks: Your Password is very bad, because it only has one of the five types, and it is super easy to be cracked by a hacker. Suggestions: M8o2@#shJD9."
if strength == 2:
    remark = "Remarks: Your Password is not really bad, but bad, because it only has two of the five types, and it is easy to be cracked by a hacker. Suggestions: C8%& $qJ6p."
if strength == 3:
    remark = "Remarks: Your Password is okay, but it still needs a little bit improvement to get an excellent password. Suggestions: 329aiOP#_%1S M"
if strength == 4:
    remark = "Remarks: Your Password is good, but still needs final touches. Suggestions: uTf_89%^-^3(."
if strength == 5:
    remark = "Remarks: Your Password is excellent and almost uncrackable! No Suggestions Found. "
print("===== This is the analyse report =====")
if strength <= 2:
    print("It looks like your password is not that strong...")
else:
    print("It looks like your password is very strong...")
print(str(nolc) + " lowercase letters!")
print(str(nouc) + " uppercase letters!")
print(str(nod) + " numeric digits!")
print(str(now)+ " whitespaces!")
print(str(nosc) + " special characters!")
print("Password Score: " + str(strength) + "/5")
print(remark)
