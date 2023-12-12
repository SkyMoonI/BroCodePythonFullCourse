# scope = the region that a variable is recognized
#         a variable is only available from inside the region it is created
#         a global and locally scoped versions of a variable can be created
# Python follows this rule to use variables
# L = Local
# E = Enclosing
# G = Global
# B = Built-in

name = "Bro" # global scope (available inside and outside functions)

def display_name():
    name = "Code" # local scope (available only inside this function)
    print(name)

display_name()
print(name)