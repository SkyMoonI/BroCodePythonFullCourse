# map() = applies a function to each item in an iterable (list, tuple, etc.)

# map(function,iterable)

#store = [("shirt", 20), ("pants", 25), ("jacket", 50), ("socks", 10), ]
#
#to_euros = lambda data: (data[0], data[1] * 0.82)  # lambda creates a new function
#to_dollars = lambda data: (data[0], data[1] / 0.82)  # lambda creates a new function
#
#store_euros = map(to_euros, store)
#store_dollars = map(to_dollars, store_euros)
#
#for i in store_euros:
#    print(i)
#
#for i in store_dollars:
#    print(i)

#topla = lambda x: x*2
#sayilar = [1, 2, 3, 4, 5]
#
#sonuclar = map(topla, sayilar)
#
#for sonuc in sonuclar:
#    print(sonuc)
