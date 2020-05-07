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
states = {
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

#
def split():
    print('-' * 30)

# print out some cities
split()
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
split()
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
split()
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
split()
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in states
split()
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
split()
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}, and has city {cities[abbrev]}")

split()

# safely get a abbreviation by state that might not be there
state = states.get('Texas')
if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")
