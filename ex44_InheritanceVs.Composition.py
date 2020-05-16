# Exercise 44: Inheritance Vs. Composition

"""
大部分使用继承的场合都可以用组合取代或简化，而多重继承则需要不惜一切地避免

什么是继承
 - 用来指明一个类的大部分或全部功能都是从一个父类中获得的。
 - 写class Foo(Bar)时，就发生了继承效果，意即「创建一个叫Foo的类，并让它继承自Bar」
     - Python让Bar的实例所具有的动作都工作在Foo的实例上。
     - 这样可以把通用的功能放到Bar里，然后再给Foo特别设定一些功能

父类和子类有3种交互方式：
 1. 子类上的动作完全等同于父类上的动作
 2. 子类上的动作完全覆盖了父类上的动作
 3. 子类上的动作部分替换了父类上的动作
"""


"""隐式继承
 - 当在父类里定义了一个函数，但没子类中定义时，会发生的隐式行为.
 - 将函数放到基类中，所有的子类将会自动获得这些函数功能。
 - 需要很多类的时候，这样可以避免重复写很多代码。
"""
class Parent(object):
    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()


"""显式覆盖
 - 当需要让子类里的函数有不同的行为时，需要覆盖子类中的函数，让它实现新功能。
 - 要做到这一点，只要在子类Child中定义一个同名的函数即可
"""
class Parent(object):
    def override(self):
        print("PARENT override()")

class Child(Parent):
    def override(self):
        print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()


"""在运行前或运行后替换
 - 使用继承的第三种方法是覆盖的一个特例
 - 这种情况下，可在父类中定义的内容运行前或之后再修改行为
 - 首先像上例一样覆盖函数，不过接着用内置函数super来调用父类Parent里的版本
"""
class Parent(object):
    def altered(self):
        print("PARENT altered()")

class Child(Parent):
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()


"""3种方式组合使用"""
print('-' * 30)
class Parent(object):
    def override(self):
        print("PARENT override()")
        
    def implicit(self):
        print("PARENT implicit()")
        
    def altered(self):
        print("PARENT altered()")

class Child(Parent):
    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()


"""要用super()的原因
 - 「多重继承」是指定义的类继承了一个或多个类
 - class SuperFun(Child, BadStuff): pass
     - 创建一个叫SuperFun的类，同时继承了Child和BadStuff两个类
     - 一旦在SuperFun实例上调用任何隐式动作，Python必须回到Child和BadStuff的类层级
       结构中查找可能的函数，而且必须用固定的顺序查找。为此Python使用了「方法解析顺序(method
       resolution order, MRO)」，和一个叫C3的算法。
     - 用super()函数在各种需要修改行为类型的场合进行处理，找到正确的函数
"""


"""super()和__init__搭配使用
 - super()最常见的用法是在基类的__init__函数中使用。通常也是唯一可进行此操作的地方，在这里
   需要在子类里做一些事情，然后在父类中完成初始化。
"""
class Child(Parent):
    def __init__(self, stuff):
        self.stuff = stuff
        super(Child, self).__init__()


"""组合
 - 继承很有用，不过还有一种实现相同功能的方法：直接使用别的类和模块
"""
class Other(object):  # 没有使用Parent，因为此处不是父类子类的A is-a B的关系，而是一个A has-a B的关系
    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Child(object):  
    def __init__(self):
        self.other = Other()  # 此处Child里有一个Other用来完成它的功能

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, BEFORE OTHER altered()")
        self.other.altered()
        print("CHILD, AFTER OTHER altered()")

print('-' * 30)

son = Child()
son.implicit()
son.override()
son.altered()


"""继承和组合的应用场合
 - 「继承与组合」的问题说到底是为了解决关于代码复用的问题。避免软件中到处都是重复的代码，既不整
   洁又没效率。
 - 继承通过创建一种在基类里隐含父类功能的机制来解决此问题
 - 组合则是利用模块和别的类中的函数调用达到相同的目的
 - 何时用哪种方案？3个指导原则
     1. 不惜一切代价避免多重继承，因为它太复杂以至于很不可靠。如果非要用，得准备好钻研类层次结
        构，以及花时间去找各种东西的来龙去脉
     2. 如果有一些代码会在不同位置和场合应用到，那就用组合把他们做成模块
     3. 只有在代码的可复用部分之间有清楚的关联，可通过一个单独的共性联系起来时，才使用继承。
"""

"""对象是不是类的副本？
 - 有的语言是这样的，如JavaScript。这种语言叫原型(Prototype)语言，此类语言里的类和对象除了用法
   以外没多少不同。
 - 在Python里类其实像是用来创建对象的模板，就跟制作硬币用到的模具一样。
"""
