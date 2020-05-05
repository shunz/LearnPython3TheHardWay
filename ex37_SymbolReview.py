# Exercise 37: Symbol Review

"""关键字"""
# and: 逻辑与
True and False == False

# as: with-as 语句一部分
# with X as Y: pass

# assert: 断言(确保)某东西为真
# assert False, "Error!"

# break: 立即停止循环
# while True: break

# class: 定义类
# class Person(object)

# continue: 停止当前循环的后续步骤，再做一次循环
# while True: continue

# def: 定义函数
# def X(): pass

# del: 从字典中删除
# del X[Y]

# elif/else: else if条件
# if: X; elif: Y; else: J

# except: 如果发生异常，运行此处代码
# except ValueError, e: print(e)

# exec: 将字符串作为Python脚本运行
exec('print("hello")')

# finally: 不管是否发生异常，都运行此处代码
# finally: pass

# for: 针对物件集合执行循环
# for X in Y: pass

# from: 从模块中导入特定部分
# from x import Y

# global: 声明全局变量
# global X

# if: if条件
# if: X; elif: Y; else: J

# import: 将模块导入到当前文件以供使用
# import os

# in: for循环的一部分，也可以X是否在Y中的条件判断
# for X in Y: pass
# 1 in [1] == True

# is: 类似于 ==，判断是否一样
1 is 1 == True

# lambda: 创建短匿名函数
s = lambda y: y**y; print(s(5))

# not: 逻辑非
not True == False

# or: 逻辑或
True or False == True

# pass: 表示空代码块
def empty(): pass

# print: 打印字符串
print('this string')

# raise: 出错后引发异常
# raise ValueError("No")

# return: 返回值并退出函数
# def X(): return Y

# try: 尝试执行代码，出错后转到except
# try: pass

# while: while循环
# while X: pass

# with: 将表达式作为一个变量，然后执行代码块
# with X as Y: pass

# yield: 暂停函数，返回到调用函数的代码中
# def X(): yield Y; X().next()


"""数据类型"""
# True/Flase: 布尔类型

# None: 表示「不存在」或「没有值」
x = None

# bytes: 字节串存储，可能是文本、PNG图片、文件等
x = b'hello'

# strings: 存储文本信息
x = 'hello'

# numbers: 存储整数
i = 100

# Floats: 存储十进制数
i = 10.389

# lists: 存储列表
j = [1, 2, 3, 4]

# dicts: 存储键-值映射
e = {'x': 1, 'y': 2}


"""字符串转移序列"""


"""老式字符串格式"""


"""运算符"""


