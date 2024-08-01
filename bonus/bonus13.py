feet_inches = input("Enter feet and inches: ")


def extract(feet_inches):
    part = feet_inches.split(" ")
    feet = float(part[0])
    inches = float(part[1])
    return {"feet": feet, "inches": inches}


def convert(feet, inches):
    meter = feet * 0.3048 + inches * 0.0254
#    return f"{feet} feet and {inches} inches is equal to {meter} meters."
    return meter


parsed = extract(feet_inches)
result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} inches is equal to {result}")

if result < 1:
    print("Kid is too small.")
else:
    print("Kid can use the slide.")