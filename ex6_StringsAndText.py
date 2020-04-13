# ex6.py
# Exercise 6: Strings and Text

types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)
print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = "False"
joke_evaluation = "Isn't that joke so funny?! {}"

# Python alse has another kind of formatting using the ".format()" syntax which you see below.
# I use it when I want to apply a format to an already created string, such as in a loop.
print(joke_evaluation.format(hilarious))  

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
