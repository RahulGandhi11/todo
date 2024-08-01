# filenames = ["1.doc", "1.report", "1.presentation"]
#
# filenames = [filename.replace('.','-')+ ".txt" for filename in filenames]
# print(filenames)
#
# new = []
# for i in [1, 2, 3]:
#     new.append(i + 10)
#
# print(new)

names = ["john smith", "jay santi", "eva kuki"]

names = [ name.title() for name in names]
print(names)

usernames = ["john 1990", "alberta1970", "magnola2000"]
usernames = [len(username) for username in usernames]
print(usernames)