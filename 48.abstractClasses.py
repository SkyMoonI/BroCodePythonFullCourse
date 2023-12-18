# prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods
# abstract method = a method that has a declaration but does not have an implementaion

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):
    def go(self):
        print("you drive the car")

    def stop(self):
        print("you stop the car")


class Motorcycle(Vehicle):
    def go(self):
        print("you drive the Motorcycle")

    def stop(self):
        print("you stop the Motorcycle")


car = Car()
motor = Motorcycle()

car.go()
motor.go()

car.stop()
motor.stop()
