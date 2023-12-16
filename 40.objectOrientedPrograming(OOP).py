from car_40 import Car

car_1 = Car("Chevy", "Corvette", 2021, "blue")
car_2 = Car("Chevy", "Mustang", 2022, "red")

print(car_1.model)
print(car_2.model)

car_2.stop()
car_1.drive()
