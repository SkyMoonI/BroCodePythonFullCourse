# super() = function used to give access to the methods of a parent class
#           returns a temporary object of a parent class when used

class Rectangle():
    def __init__(self, length, witdh):
        self.length = length
        self.witdh = witdh


class Square(Rectangle):
    def __init__(self, length, witdh):
        super().__init__(length, witdh)

    def area(self):
        return self.length * self.witdh


class Cube(Rectangle):
    def __init__(self, length, witdh, height):
        super().__init__(length, witdh)
        self.height = height

    def volume(self):
        return self.length * self.witdh * self.height


square = Square(3, 3)
cube = Cube(4, 4, 4)

print(square.area())
print(cube.volume())
