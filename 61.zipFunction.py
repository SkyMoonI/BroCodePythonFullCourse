# zip(*iterable) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                  creates a zip object with paired elements stored in tuples for each element

usernames = ["dude", "bro", "mister"]
passwords = ("password1", "password2", "password3")
login_date = ["1/1/20", "1/2/21", "1/3/22"]

# users = zip(usernames, passwords)
# users = list(zip(usernames, passwords))
# users = dict(zip(usernames, passwords))
# users = zip(usernames, passwords, login_date)

# print(type(users))
# for i in users:
#    print(i)

# for key,value in users.items():
#    print(key,value)
