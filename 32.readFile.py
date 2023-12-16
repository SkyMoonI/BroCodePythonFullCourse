# with open("C:\\Users\\iseri\\PycharmProjects\\pythonFullCourseForBeginnersBroCode\\test.txt")

try:
    with open("test.txt") as file:  # closes the file automatically
        print(file.read())
except FileNotFoundError as e:
    print(e)
    print("That file was not found")

# print(file.closed)  # return True if the file is closed
