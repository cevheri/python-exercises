# python Object Oriented Programming
#
# Object
# ref : http://python-history.blogspot.com/2009/02/first-class-everything.html

class A:
    def __init__(self, x):
        self.x = x

    def spam(self, y):
        print(self.x, y)

a = A("Guido Van Rossum")
print(a.x)
print(a.spam("Python"))
s = a.spam("Python Blog")
print(s)

def func_1():
    return A(1)
print(func_1())

print(A(1))
#######################################
class CustomClass:
    pass


c1 = CustomClass()  # Generate Object
print(dir(c1))

print("-" * 30)
print()


# Class Attribute
# init method
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']
##############################################
#
# Custom Class Definition
class CustomClass2():
    class_attribute = "class_attribute"
    print("Class Attribute")

    def __init__(self):
        self.instance_attribute = "instance_attribute"
        print("init method")

    def instance_method(self):
        print("instance method")

    @classmethod
    def class_method(cls):
        print("Class Method")

    @staticmethod
    def static_method():
        print("Static Method")


c2 = CustomClass2()  # generate object
print(dir(c2))

print("-" * 30)
print()
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
# 'class_attribute', 'class_method', 'instance_attribute', 'instance_method', 'static_method']
##############################################


