# classes in python


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def greet(self) -> None:
        print(f"Hello, {self.name} of age {self.age}")


p1 = Person("dick", 1)
p1.greet()

print(p1.name)


# inheritance


class Animal:
    def __init__(self, species):
        self.species = species

    def sound(self) -> None:
        print("some generic animal sound")


class Dog(Animal):
    def sound(self):
        print("Woof")


animal = Animal(None)
animal.sound()

dog = Dog("Canine")
dog.sound()

print("scope test ---------------")


"""
Python resolves names using the so-called LEGB rule,
which is named after the Python scope for names.
The letters in LEGB stand for: 
    Local - Enclosing - Global - Built-in
"""


def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
        # `nonlocal` allows the inner function to modify
        # the value of the outer function's variable
        # so spam = "test spam" will get re-assigned to
        #   spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"
        # With global, you're telling Python to use the globally
        # defined variable instead of locally creating one

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    """
    It causes the variable to refer to the previously bound variable
    in the closest enclosing scope.
    In other words, it will prevent the variable from trying 
    to bind locally first,and force it to go a level 'higher up'
    
    """
    print("After nonlocal assignment:", spam)
    # result: After nonlocal assignment: nonlocal spam
    do_global()
    print("After global assignment:", spam)
    # After global assignment: nonlocal spam
    """
    This does not print `global spam` due to the previous
    """


scope_test()
print("In global scope:", spam)
