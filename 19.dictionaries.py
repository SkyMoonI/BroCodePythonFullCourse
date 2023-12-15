# dictionary = a changeable, unordered collection of unique key:value pairs
#              fast because they use hashing, allow us to access a value quickly

capitals = {'USA': 'Washington DC',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow'}

# capitals.update({'Germany':'Berlin'})
# capitals.update({'USA':'TOKAT'})
# capitals.pop("China") # removes china
# capitals.clear()

# print(capitals['USA'])
# print(capitals['Germany'])
# print(capitals.get('Germany')) # safer to call with get
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

# for key, value in capitals.items():
#    print(key, value)
