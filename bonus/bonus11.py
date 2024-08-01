def get_average():
    with open("files/data.txt", 'r') as file:
        data = file.readlines()
    values = data[1:]
    values = [float(i) for i in values] #List comprehenssion

    average_local = sum(values) / len(values)
    return average_local


average = get_average()
print(average)


def get_max():
    grades = [9.6, 9.2, 9.7]
    max_local = max(grades)
    return max_local

max = get_max()
print(max)
