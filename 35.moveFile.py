import os

source = "test.txt"
destination = "C:\\Users\\iseri\\PycharmProjects\\pythonFullCourseForBeginnersBroCode\\test\\test.txt"

try:
    if os.path.exists(destination):
        print("there is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError:
    print(source + " was not found")
