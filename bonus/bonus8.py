# CHeck if password is secure
password = input("Enter new password: ")
result = []

if len(password) >= 8:
    result.append(True)

else:
    result.append(False)

digit = False
for i in password:
    if i.isdigit():
        digit = True

result.append(digit)

upper = False
for i in password:
    if i.isupper():
        upper = True

result.append(upper)

if all(result):
    print("Strong Password")
else:
    print("Weak Password")

##############################################################
print("Run the Dicitonary password")
password = input("Enter new password: ")
result = {}

if len(password) >= 8:
    result["length"] = True

else:
    result["length"] = False

digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digit"] = digit

upper = False
for i in password:
    if i.isupper():
        upper = True

result["upper-case"] = upper

print(result)

if all(result.values()):
    print("Strong Password")
else:
    print("Weak Password")