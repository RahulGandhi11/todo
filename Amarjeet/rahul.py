import json

with open("work.json", 'r') as f:
    data = json.load(f)
    # first_item = data[0]

print(data["key"])
