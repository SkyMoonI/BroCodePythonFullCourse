class Animal:
    alive = True

    def eat(self):
        print("This animal is eating")

    def sleep(self):
        print("This animal is sleeping")


class Rabit(Animal):
    def run(self):
        print("This rabbit is running")


class Fish(Animal):
    def swim(self):
        print("This fish is swimming")


class Hawk(Animal):
    def fly(self):
        print("This hawk is flying")


rabit = Rabit()
fish = Fish()
hawk = Hawk()

print(rabit.alive)
fish.eat()
hawk.sleep()
rabit.run()
fish.swim()
hawk.fly()


