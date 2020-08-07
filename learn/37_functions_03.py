# lambda
#
def f1(param1, param2):
    return param1 + param2


f1(2, 4)  # 6

f2 = lambda param1, param2: param1 + param2
f2(2, 4)  # 6

##############################################
chars = "abcçdefgğhıijklmnoöprsştuüvyz"
translate = {i: chars.index(i) for i in chars}

names = ["ahmet", "ışık", "ismail", "çiğdem",
         "can", "şule", "iskender"]

# tr lang sort
# example 1
print(sorted(names, key=lambda x: translate.get(x[0])))


##################################
# example 2
def custom_sort(eleman):
    return translate.get(eleman[0])


print(sorted(names, key=custom_sort))


##################################
# even number
# example 1
def is_even(p):
    return p % 2 == 0


print(is_even(10))  # True
print(is_even(9))  # False

# example 2
is_even2 = lambda p: p % 2 == 0
print(is_even2(10))  # True
print(is_even2(9))  # False
################################
# square of the number
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#########################
# example 1 :
for i in l:
    print(i ** 2)

#########################
# example 2 :
print([i ** 2 for i in l])  # [1, 4, 9, 16, 25, 36, 49, 64, 81]

#########################
# example 3 :
print(*map(lambda number: number ** 2, l))  # 1 4 9 16 25 36 49 64 81
print()


#########################
# example 4
def square(p):
    return p ** 2


print(*map(square, l))  # 1 4 9 16 25 36 49 64 81
print()
#########################
# split
# example 1
custom_split1 = lambda val, splitter: splitter.join(val.split())

print(custom_split1("Python Programming Language", "; "))
print()


# example 2
def custom_split2(val, splitter):
    return splitter.join(val.split())


print(custom_split1("Python Programming Language", "; "))
print()
# User Interface
#
import tkinter
import tkinter.ttk as ttk

pen = tkinter.Tk()

# example 1
btn = ttk.Button(text="hello", command=lambda: print("Hello"))
btn.pack(padx=20, pady=20)


# pen.mainloop()
#

# example 2
def hello():
    print("Hello")


btn = ttk.Button(text="hello", command=hello)
btn.pack(padx=20, pady=20)
# pen.mainloop()
print()

#############################################
# Recursive Functions
print("Recursive Functions")


def rec_func(p):
    if len(p) < 1:
        return p
    else:
        print(p)
        rec_func(p[1:])


print(rec_func("Python"))
print()
# reverse
print("reverse")


def custom_reverse(val):
    if len(val) < 1:
        return val
    else:
        custom_reverse(val[1:])
        print(val[0])


print(custom_reverse("python"))


##
def custom_reverse(val):
    if len(val) < 1:
        return val
    else:
        return custom_reverse(val[1:]) + val[0]


print(custom_reverse("python"))
print()


# counter
# example 1
def counter(number, limit):
    print(number)
    if number == limit:
        return "Done"
    else:
        return counter(number + 1, limit)
        print(number)


print(counter(0, 10))
###################################
l = [1, 2, 3, [4, 5, 6], [7, 8, 9, [10, 11], 12], 13, 14]


# ==> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

def convert_flat_list(lst):
    if not isinstance(lst, list):
        return [lst]
    elif not lst:
        return []
    else:
        return convert_flat_list(lst[0]) + convert_flat_list(lst[1:])


l = [1, 2, 3, [4, 5, 6], [7, 8, 9, [10, 11], 12], 13, 14]

print(convert_flat_list(l))


#
def custom_sum(numbers):
    if len(numbers) < 1:
        return 0
    else:
        first, last = numbers[0], numbers[1:]  # !!!
        first, *last = numbers  # !!!!
        return first + custom_sum(last)


l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(custom_sum(l))


# Nested Functions
#


def fonk1():  # enclosing function
    #
    def fonk2():  # nested function
        pass


##
def printer():
    def do_print(val):
        print(val)

    return do_print


y = printer()
y("Test")
z = printer()
z("Test")
print(type(y))  # <class 'function'>
print(y)  # <function printer.<locals>.do_print at 0x7f8686eb95e0>
print(z)  # <function printer.<locals>.do_print at 0x7fd9d4a13670>
#  y!=z
################
# nonlocal
print("nonlocal")


# local
def printer2():
    val = "Hello"

    def do_print():
        val = " World"
        print(val)

    return do_print


y2 = printer2()
y2()  # World


#######################
# nonlocal
def printer2():
    val = "Hello"

    def do_print():
        nonlocal val  # !!!
        val += " World"
        print(val)

    return do_print


y2 = printer2()
y2()  # World


#################
def counter():
    count = 0

    def do_dount():
        nonlocal count
        count += 1
        return count

    return do_dount


a = counter()
print(a())  # 1
print(a())  # 2
print(a())  # 3
b = counter()
print(b())  # 1
print(b())  # 2
print(b())  # 3
#################
# some
count2 = 0


def counter2():
    global count2
    count2 += 1
    print(count2)


c = counter2
c()  # 1
c()  # 2


# nested function example
# bad
def dosyadaki_karakter_sayısı(dosya, karakter):
    sonuç = 0

    if type(dosya) == str:
        with open(dosya, "r") as f:
            veri = f.read()
            for i in veri:
                if i == karakter:
                    sonuç += 1
    else:
        veri = dosya.read()
        for i in veri:
            if i == karakter:
                sonuç += 1

    return sonuç


##############################################
# good
def dosyadaki_karakter_sayısı(dosya, karakter):
    def karakter_sayısı(karakter_dizisi):
        sayaç = 0
        for i in karakter_dizisi:
            if i == karakter:
                sayaç += 1
        return sayaç

    if type(dosya) == str:
        with open(dosya, "r") as f:
            return karakter_sayısı(f.read())
    else:
        return karakter_sayısı(dosya.read())


# generators
# yield nex
lst = [i for i in range(10)]


def counter3():
    number = 0
    while True:
        number += 1
        yield number


print(type(counter3))  # <class 'function'>
c = counter3()
print(c)  # <generator object counter3 at 0x7fd432321b30>

print(next(c))  # 1
print(next(c))  # 2


####
def generator():
    yield "Hello"
    yield "World"


g = generator()
print(next(g))
print(next(g))
# print(next(g)) #StopIteration ERROR

# fibonacci
print("fibonacci")


def fibonacci():
    x = 1
    y = 0
    z = 0
    while True:
        z = y
        y = x
        x = y + z
        yield x
        if x > 100:
            return


f = fibonacci()
print(next(f))  # 1
print(next(f))  # 2
print(next(f))  # 3
print(next(f))  # 5
print(next(f))  # 8
print(next(f))  # 13

for i in fibonacci():
    print(i)


#    if i>100:
#        break
#
# yield example
def do_print(n):
    for i in range(n):
        print("Yield Function")
        yield


y = do_print(5)
for i in y:
    pass
print()
# yield from
print("yield from")


def generator1():
    yield "Generator 1 start"
    yield "Generator 1 stop"
def generator2():
    yield "Generator 2 start"
    yield from generator1()
    yield "Generator 2 stop"
for i in generator2():
    print(i)

# or
def generator1():
    yield "Generator 1 start"
    yield "Generator 1 stop"
def generator2():
    yield "Generator 2 start"
    # yield from generator1()
    for i in generator1():
        yield i
    yield "Generator 2 stop"
print()
# list generator
print("List Generators")
lst = [i for i in range(10)]
print(type(lst)) # <class 'list'>

generator = (i for i in range(10))
print(type(generator)) # <class 'generator'>
# or
def generator_function():
    for i in range(10):
        yield i

print(type(generator_function)) # <class 'generator'>
g = generator_function()
print(type(g)) # <class 'generator'>


g1  =(i for i in range(3))
print(list(g1)) # [0, 1, 2]
print(list(g1)) # []

g2  =[i for i in range(3)]
print(list(g2)) # [0, 1, 2]
print(list(g2)) # [0, 1, 2]


g3  =(i for i in range(3))
l = list(g3)
print(l) # [0, 1, 2]
print(l) # []

g5 = ((str(i),i) for i in range(3))
d = {}
for key,value in g5:
        d[key] = value
print(d)