import os
import shutil

path = "test.txt"

try:
    os.remove(path)  # can't remove directories
#    os.rmdir(path)  # can remove empty directories
#    shutil.rmtree(path)  # can remove directories with items
except FileNotFoundError:
    print("that file was not found")
except PermissionError:
    print("You do not have permisson to delete that")
except OSError:
    print("There is files in that folder, you cannot delete")
else:
    print(path + " was deleted")