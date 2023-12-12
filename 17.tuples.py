# tuple = collection which is ordered and unchangeable
#         used to group together related data

student = ("Bro", 21, "male")

print(student.count("Bro")) # counts how many times tuple has the item, case sensetive
print(student.index("male")) # checks the index of the item
for x in student:
    print(x)

if "Bro" in student:
    print("Bro is here!")