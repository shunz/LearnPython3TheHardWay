# Exercise 16: Reading And Writing Files

"""与文件相关的命令
close: 关闭文件
read：读取文件的内容，可以把结果赋给一个变量
readline: 只读取文本文件中的一行
truncate: 清空文件
write('stuff'): 将stuff写入文件
seek(0): 将读写位置移动到文件开头
"""

from sys import argv
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
input("?")
print("Opening the file...")

target = open(filename, 'r+')
print(f"Here's the file content:\n\"")
print(target.read())
print("\"\nTruncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print("And finally, we close it.")
target.close()
