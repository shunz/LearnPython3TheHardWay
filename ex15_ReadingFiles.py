# Exercise 15: Reading Files

from sys import argv
scrpt, filename = argv

txt = open(filename)
print(f"Heres your file {filename}:")
print(txt.read())
print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again)
print(txt_again.read())
