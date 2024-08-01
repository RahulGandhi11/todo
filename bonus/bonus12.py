# feet_inches = input("Enter feet and inches: ")
#
#
# def convert(feet_inches):
#     part = feet_inches.split(" ")
#     feet = float(part[0])
#     inches = float(part[1])
#
#     meter = feet * 0.3048 + inches * 0.0254
# #    return f"{feet} feet and {inches} inches is equal to {meter} meters."
#     return meter
#
#
# result = convert(feet_inches)
#
#
# if result < 1:
#     print("Kid is too small.")
# else:
#     print("Kid can use the slide.")


def strength(password):
    result = {}
    if len(password) >=8:
        result["length"] = True
    else:
        result["length"] = False

    digit = False
    uppercase = False

    for i in password:
        if i.isdigit():
            digit = True

        if i.isupper():
            uppercase = True

        result["digits"] = digit
        result["upper-case"] = uppercase

    if all(result.values()):
        return "Strong Password"
    else:
        return "Weak Password"

print(strength("RahulGandhi1"))