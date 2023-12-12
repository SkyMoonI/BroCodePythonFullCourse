# str.format() = optional method that gives users
#                more control when displaying output

#animal = "cow"
#item = "moon"
#
#print("the " + animal + " jumped over the " + item)
#print("the {} jumped over the {}".format(animal,item))
#print("the {1} jumped over the {0}".format(animal,item)) # positinal argument
#print("the {animal} jumped over the {item}".format(animal="cow",item="moon"))
#
#text = "the {} jumped over the {}"
#print(text.format(animal,item))


#name = "Bro"
#
#print("Hello, my name is {}".format(name))
#print("Hello, my name is {:10}. nice to meet you".format(name))
#print("Hello, my name is {name:10}. nice to meet you".format(name="cool"))
#print("Hello, my name is {:<10}. nice to meet you".format(name)) # left align by default
#print("Hello, my name is {:>10}. nice to meet you".format(name)) # right align
#print("Hello, my name is {:^10}. nice to meet you".format(name)) # center

number = 1000000

print("the number is {:.2f}".format(number))
print("the number is {:.3f}".format(number))
print("the number is {:,}".format(number))
print("the number is {:b}".format(number))
print("the number is {:o}".format(number))
print("the number is {:x}".format(number))
print("the number is {:E}".format(number))
print("the number is {:e}".format(number))
