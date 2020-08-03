# functions : custom functions

def func_name(param1, param2):
    print(param1, param2)


func_name("Python", "Language")


def sysinfo():
    import sys
    print("\nPython;")
    print("\tMajor version :", sys.version_info.major)
    print("\tMinor version :", sys.version_info.minor)
    print("\tMicro version :", sys.version_info.micro)

    print("\nOS;")
    print("\tName:", sys.platform)


sysinfo()


# name param
def len2(val):
    c = 0
    for s in val:
        c += 1
    print(c)


len2(val="Python Programming Language")
len2("Python")
len2(dir(str))


# default param
def hi(val="Hello"):
    print(val)


hi()
hi("Hi")


# arg param
def rand(*args):
    print(args)


rand()
rand(1)
rand(1, 2, 3, 4, 5, 6, 7, 8, 9, 0, ".", ".")


# name arg param
def rand_names(**kwargs):
    print(kwargs)


rand_names(name="Cevheri", language="Python", ide="PyCharm")


# extended print example
def print2(*args, start='', **kwargs):
    for val in args:
        print(start + val, **kwargs)


print2('val1', 'val2', 'val3', start="#.")


# return val

def add(number1, number2):
    return number1 + number2


print(add(127, 128))


######################################
def func():
    print(3)
    return
    print(5)


func()

######################################
# sample
import random


def generate_number(start=0, stop=500, piece=6):
    numbers = set()
    while len(numbers) < piece:
        numbers.add(random.randrange(start, stop))
    return numbers


for r in range(10):
    print(generate_number())

######################################
# global variable
x = 0


def func():
    x = 1
    return x


print(func())  # 1
print(x)  # 0 !!!!!!!!!

######################################
# but

x = 0


def func():
    print(x)


func()  # 0# :)))))
######################################
"""
error
name = 'python'


def func():
    name += ' language'
    return name


print(func())
"""