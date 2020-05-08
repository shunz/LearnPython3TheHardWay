# Exercise 40: Modules, Classes and Objects

mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])  # get apple from dict

import ex40_mystuff
ex40_mystuff.apple()  # get apple frome module
print(ex40_mystuff.tangerine)  # same thing, it's just a variable.


class MyStuff(object):
    def __init__(self):  
        self.tangerine = "And now a thousand years between."

    def apple(self):
        print("I AM CLASSY APPLES!")

thing = MyStuff()
thing.apple()  # get apple from class
print(thing.tangerine)

print('-' * 40)

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

print('-' * 40)

Twinkle_Lyrics = ["Twinkle Twinkle little stars",
                  "How I wonder what you are"]
Twinkle_Stars = Song(Twinkle_Lyrics)
Twinkle_Stars.sing_me_a_song()


"""
Q: 为什么创建__init__或者别的类函数时需要多加一个self变量
A：如果不加self, 则cheese='Frank'这样的代码就会有歧义，它指的既可能是实例的
   cheese属性，也可能是一个局部变量。而有了self.cheese = 'Frank'就清楚的
   知道这指的是实例的属性self.cheese
"""
