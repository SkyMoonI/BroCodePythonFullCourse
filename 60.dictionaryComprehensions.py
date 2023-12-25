# dictionary comprehension = create dictionaries using an expression
#                            can replace for loops and certain lambda functions

# dictionary = {key: expression for (key,value) in iterable}
# dictionary = {key: expression for (key,value) in iterable if conditional}
# dictionary = {key: expression if/else for (key,value) in iterable}

cities_in_F = {"new york":32, "boston": 75, "los angeles": 100, "chicago": 50}

cities_in_C = {key: ((value-32)*(5/9)) for(key,value) in cities_in_F.items()}
print(cities_in_C)

cities_in_C2 = {key: ((value-32)*(5/9)) for(key,value) in cities_in_F.items() if ((value-32)*(5/9)) >= 15}
print(cities_in_C2)

cities_in_C3 = {key: "warm" if value > 50 else "cold" for(key,value) in cities_in_F.items() }
print(cities_in_C3)

def check_temp(value):
    if value >= 70:
        return "hot"
    elif value >=50 or value <70:
        return "warm"
    else:
        return "cold"

cities_in_C4 = {key: check_temp(value) for(key,value) in cities_in_F.items() }
print(cities_in_C4)