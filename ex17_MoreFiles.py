# Exercise 17: More Files

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("ready, hit RETURN to continue, CTRL-C to abort.")
input()
out_file = open(to_file, 'w')
out_file.write(indata)

print("Allright, all done.")

out_file.close()
in_file.close()


'''First make a sample file in the command line'''
# echo "This is a test file." > test.txt

'''then look at it'''
# cat test.txt

'''now run our script on it'''
