class Car:
    color = None

class Motorcycle:
    color = None

def change_color(vehicle, color):
    vehicle.color = color

car_1=Car()
motor=Motorcycle()

print(car_1.color)
print(motor.color)

change_color(car_1, "red")
change_color(motor, "blue")

print(car_1.color)
print(motor.color)
