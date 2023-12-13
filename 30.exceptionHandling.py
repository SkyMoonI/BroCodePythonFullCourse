# exception = events detected during that interrupt the flow of a program

try:
    numerator = int(input("Enter a number to divide: "))
    denumerator = int(input("Enter a number to divide by: "))
    result = numerator / denumerator
except ZeroDivisionError as e:
    print(e) # prints about exepction
    print("You can't divide by zero!")
except ValueError as e:
    print(e)
    print("Enter only numbers pls")
except Exception as e: # at any error, this is executed
    print(e)
    print("Something went wrong!")
else:
    print(result)
finally:
    print("This will always execute")
