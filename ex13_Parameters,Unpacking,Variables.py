# Exercise 13: Parameters, Unpacking, Variables

from sys import argv  # argv = argument variableq
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
      
# run this file in command line
# python3 ex13.py 1st 2nd 3rd
