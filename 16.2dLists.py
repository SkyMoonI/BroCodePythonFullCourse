# 2d lists = a list of lists

drinks = ["coffee", "soda", "tea"]
dinner = ["pizza", "hamburger", "hotdog"]
dessert = ["cake", "ice cream"]

foods = [drinks, dinner, dessert]

print(foods[0][1])

for food in foods:
    for i in food:
        print(i, end=" ")
    print()