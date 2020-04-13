# ex5.py
# Exercise 5: More Variables and Printing

# f-string(format string)

name = 'Zed A. shaw'
age = 35  # not a lie
height = 74  # inches
weight = 180  # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talke about {name}.")
print(f"He's {height} inches / {height * 2.54} cm tall.")
print(f"He's {weight} pounds / {weight * 0.4536} kg heavy.")
print("Acturally that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f'His teech are usually {teeth} depending on the coffee.')

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight}, I get {total}.")

