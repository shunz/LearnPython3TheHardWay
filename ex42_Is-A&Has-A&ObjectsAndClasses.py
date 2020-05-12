# Exercise 42: Is-A, Has-A, Objects and Classes

# is-a(是什么)用在讨论「两者以类的关系相互关联」的时候，比如：鱼和泥鳅的关系
# has-a(有什么)用在「两者无共同点，仅是互为参照」的时候，比如：泥鳅和鳃的关系

# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(ojbect):
    pass

# Dog is-a object
class Dog(Animal):
    def __init__(self, name):
        # Dog has-a name
        self.name = name

# Cat is-a object
class Cat(Animal):
    def __init__(self, name):
        # Cat has a name
        self.name = name

# Person is-a object
class Person(object):
    def __init__(self, name):
        # Person has-a name
        self.name = name
        # Person has-a pet of some kind
        self.pet = None

# Employee is-a object
class Employee(Person):
    def __init__(self, name, salary):
        # Employee has-a name
        super(Employee, self).__init__(name)
        # Employee has-a salary
        self.salary = salary

# Fish is-a objectn
class Fish(object):
    pass

# Salmon is-a object
class Salmon(Fish):
    pass

# Halibut is-a object
class Halibut(Fish):
    pass

# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")

# mary has-a pet
mary.pet = satan

# frank is-a Employee, and has-a salary
frank = Employee("Frank", 120000)

# frank has-a pet
frank.pet = rover

# flipper is-a Fish
flipper = Fish()

# crouse is-a Salmon()
crouse = Salmon()

# harry is-a Halibut()
harry = Halibut()
