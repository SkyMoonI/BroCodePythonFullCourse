# Duck typing = concept where the class of an object is less important then the methods/attributes
#               class type is not checked if minumum methods/attributes are present
#               "if it walks like a duck, and it quacks like a duck, then it must be a duck

class Duck:
    def walk(self):
        print("this duck is walking")

    def talk(self):
        print("this duck is talking")


class Chicken:
    def walk(self):
        print("this Chicken is walking")

    def talk(self):
        print("this Chicken is talking")


class Person:
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("you caught the critter!")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
