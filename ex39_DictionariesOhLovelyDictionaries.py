# Exercise 39: Dictionaries, Oh Lovely Dictionaries

things = ['a', 'b', 'c', 'd']
print(things[1])
things[1] = 'z'
print(things[1])
print(things)

stuff = {'name': 'Shunz', 'age': 20, 'height': 6*12+2}

print(stuff['name'])
print(stuff['age'])
print(stuff['height'])

stuff['city'] = "Chengdu"
print(stuff['city'])
print(stuff)

stuff[1] = "Wow"
stuff[2] = "Neato"
print(stuff[1])
print(stuff)

del stuff[2]
print(stuff)

[print() for _ in range(3)]


# create a mapping of state of abbreviation
state = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 30)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])
