# keyword arguments = arguments preceded by an identifier when we pass the to a function
#                     the order of the arguments doesn't matter, unlike positional arguments
#                     python knows the names of the arguments that our function receive

def Hello(first,middle,last):
    print("hello " + first + " " + middle + " " + last)

Hello(middle="dude", last="code", first="bro")

