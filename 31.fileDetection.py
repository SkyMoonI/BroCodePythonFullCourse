import os
path = "C:\\Users\\iseri\\PycharmProjects\\pythonFullCourseForBeginnersBroCode\\test.txt"

if os.path.exists(path):
    print("That location exists")
    if os.path.isfile(path):
        print("That is a file")
    elif os.path.isdir(path):
        print("That is a directory")
else:
    print("that location doesn't exists")