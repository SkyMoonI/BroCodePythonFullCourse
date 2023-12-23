# Higher order functions = a function that eighter:
#                          1. accepts a function as an argument
#                           or
#                          2. returns a function
#                          (in python, functions are also treated as objects)

# def loud(text):
#    return text.upper()
# def quiet(text):
#    return text.lower()
#
# def hello(func):
#    text = func("Hello")
#    print(text)
#
# hello(loud)
# hello(quiet)

#def divisor(x):
#    def dividend(y):
#        return y / x
#
#    return dividend
#
#
#divide = divisor(2)
#quotients = divide(10)
#print(quotients)
#
#
#def topla(a, b):
#    def carp(x, y):
#        return x * y
#
#    return carp(a, b)
#
#
#print(topla(2, 3))
#
#def dis():
#    isim = "Ali"
#    def ici():
#        print(isim)
#    ici()
#
#dis()

#def topla(a, b):
#    def carp(x, y):
#        return x * y
#    return carp(a, b)
#
#def baska_bir_fonksiyon():
#    print(topla(2, 3))
#
#baska_bir_fonksiyon()
 