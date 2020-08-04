# builtin functions


"""
abs()
round()
all()
any()
ascii()
repr()
bool()
bin()
bytes()
bytearray()
chr()
list()
set()
tuple()
frozenset()
complex()
float()
int()
str()
dict()
callable()
ord()
oct()
hex()
eval(), exec(), globals(), locals(), compile()
copyright()
credits()
license()
dir()
divmod()
enumerate()
exit()
help()
id()
input()
format()
filter()
hash()
isinstance()
len()
map()
max()
min()
open()
pow()
print()
quit()
range()
reversed()
sorted()
slice()
sum()
type()
zip()
vars()
"""

# abs
print("abs()")
abs(-20)  # 20
abs(20)  # 20
abs(20.0)  # 20.0
abs(20 + 3j)  # 20.223748416156685

# round
print("round()")
round(12.4)  # 12
round(12.7)  # 13
round(1.5)  # 2 !!!!!!!!!!!
round(12.5)  # 12 !!!!!!!!!

22 / 7  # 3.142857142857143
round(22 / 7)  # 3
round(22 / 7, 0)  # 3.0
round(22 / 7, 1)  # 3.1
round(22 / 7, 2)  # 3.14
round(22 / 7, 3)  # 3.143
round(22 / 7, 4)  # 3.1429

# all
print("all()")
l = [1, 2, 3, 4]
print(all(l))  # True

l1 = [0, 1, 2, 3, 4]
all(l1)  # False
l2 = ['ahmet', 'mehmet', '']
all(l2)  # False

a = 3
t1 = a == 3  # 3? True
t2 = a < 4  # < 4? True
t3 = a % 2 == 1  # mod = 1 True
all([t1, t2, t3])  # True

# any
print("any()")
l = [1, 2, 3, 4]
print(all(l))  # True

l1 = [0, 1, 2, 3, 4]
all(l1)  # True
l2 = ['ahmet', 'mehmet', '']
all(l2)  # True

l = ['', 0, [], (), set(), dict()]
any(l)  # False

# ascii
print("ascii()")

a = "Python"
print(ascii(a))  # Python
print(ascii('\n!'))  # '\n'

print(ascii("CEVHERİ"))
# unicode 'CEVHER\u0130'

# repr
print("repr()")

print(ascii("CEVHERİ"))
# unicode 'CEVHER\u0130'
# but
print(repr("CEVHERİ"))  # 'CEVHERİ'
print(repr('\n!'))  # '\n!'

# bool
print("bool()")

bool(0)  # False
bool(1)  # True
bool([])  # False

# bin
print("bin()")
bin(12)  # '0b1100'

# bytes
print("bytes()")
print(bytes(12))  # b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

print(bytes("CEVHERİ", encoding="utf-8"))  # b'CEVHER\xc4\xb0'
print(bytes("CEVHERİ", encoding="cp1254"))  # b'CEVHER\xdd'
print(bytes("CEVHERİ", encoding="cp857"))  # b'CEVHER\x98'
print(bytes("CEVHERİ", encoding="ascii", errors="replace"))  # b'CEVHER?'

bytes([65, 10, 12, 11, 15, 66])  # b'A\n\x0c\x0b\x0fB'
# 0-127= ascii table
# 128-256 = latin-1 table


# bytearray
print("bytearray()")
ba = bytearray("CEVHERİ", encoding="utf-8")  # bytearray(b'CEVHER\xc4\xb0')
print(ba[0])  # 67

# chr -> using unicode
print("chr()")
chr(10)  # '\n'
chr(65)  # 'A'
chr(305)  # 'ı'

# list
print("list()")
l = list()
print(list("python"))  # ['p', 'y', 't', 'h', 'o', 'n']
s = {'a': 44, 'b': 10, 'c': 100}
print(list(s))  # ['a', 'b', 'c']
print(list(s.values()))  # [44, 10, 100]

# set
print("set()")
k = set()
i = "python"
print(set(i))  # {'y', 'o', 't', 'n', 'p', 'h'}

# tuple
print("tuple()")
k = tuple("cev")
print(type(k))  #
print(k)  # ('c', 'e', 'v')

# frozenset
print("frozenset()")
s = set('frozenset')
df = frozenset(s)
print(df)  # frozenset({'s', 't', 'e', 'f', 'z', 'r', 'o', 'n'})

# complex = 12+0j
print("complex()")

print(complex(15))  # (15+0j)
complex(15, 2)  # (15+2j)

# float
print("float()")
float('134')  # 134.0
float(12)  # 12.0

# int
print("int()")
print(int('134'))  # 133
print(int(12.5))  # 12
print(int('12', 8))  # 10
print(int('4cf', 16))  # 1231

# str
print("str()")
str(12)  # '12'

byte = b'Python'
val = str(byte, encoding="utf-8", errors="ignore")
print(val)  # Python

# dict
print("dict()")
d = dict()

s = dict(a=1, b=2, c=3)  # {'a': 1, 'b': 2, 'c': 3}
elements = (['a', 1], ['b', 2], ['c', 3])
dict(elements)  # {'a': 1, 'b': 2, 'c': 3}

# callable
print("callable()")
callable(open)  # True

import sys

callable(sys.version)  # False

# ord
print("ord()")
ord('a')  # 97
ord('ı')  # 305

# oct
print("oct()")
oct(10)  # '0o12'

# hex
print("hex()")
hex(305)  # 'Ox131'

###############################################33
# eval(), exec(), globals(), locals(), compile()
# eval('a = 5') wrong statement
eval('5 + 25')  # 30 !!!!!!!! expression

a = 20
exec('a = 5')
print(a)  # 5 :)))

# globals
print(globals())

globals()['a'] = 23
print(a)  # 23


# locals
def func(param1, param2):
    x = 10
    print(locals())  # {'param1': 10, 'param2': 20, 'x': 10}


func(10, 20)

name_space = {}
exec("a=8", name_space)

# copyright
print("copyright()")
print(copyright())
# Copyright (c) 2001-2020 Python Software Foundation.
# All Rights Reserved.
#
# Copyright (c) 2000 BeOpen.com.
# All Rights Reserved.
#
# Copyright (c) 1995-2001 Corporation for National Research Initiatives.
# All Rights Reserved.
#
# Copyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.
# All Rights Reserved.
# None


# credits
print("credits()")
print(credits())
# Thanks to CWI, CNRI, BeOpen.com,
# Zope Corporation and a cast of thousands
# for supporting Python development.
# See www.python.org for more information.


# license
print("license()")
# print(license())
# A. HISTORY OF THE SOFTWARE
# ==========================
#
# Python was created in the early 1990s by Guido van Rossum at Stichting
# Mathematisch Centrum (CWI, see http://www.cwi.nl) in the Netherlands
# as a successor of a language called ABC.  Guido remains Python's
# principal author, although it includes many contributions from others.
#
# In 1995, Guido continued his work on Python at the Corporation for
# National Research Initiatives (CNRI, see http://www.cnri.reston.va.us)
# in Reston, Virginia where he released several versions of the
# software.
#
# In May 2000, Guido and the Python core development team moved to
# BeOpen.com to form the BeOpen PythonLabs team.  In October of the same
# year, the PythonLabs team moved to Digital Creations, which became
# Zope Corporation.  In 2001, the Python Software Foundation (PSF, see
# https://www.python.org/psf/) was formed, a non-profit organization
# created specifically to own Python-related Intellectual Property.
# Zope Corporation was a sponsoring member of the PSF.
#
# All Python releases are Open Source (see http://www.opensource.org for
# the Open Source Definition).  Historically, most, but not all, Python
# Hit Return for more, or q (and Return) to quit: q
# None

# dir
print("dir()")
print(dir())
# ['__annotations__', '__builtins__', '__cached__',
# '__doc__', '__file__', '__loader__',
# '__name__', '__package__', '__spec__',
# 'a', 'ba', 'byte', 'd', 'df', 'elements', 'func', 'i', 'k', 'l', 'l1', 'l2', 'name_space', 's', 'sys', 't1', 't2', 't3', 'val']

dir('')
dir([])
dir({})

# divmod
print("divmod()")
print(divmod(10, 2))  # (5,0)
# (10/2 = 5, 10%2 = 0)
divmod(10, 3)  # (3, 1)

# enumerate
print("enumerate()")

print(enumerate("enumerate"))  # <enumerate object at 0x7f43d25548c0>
print(list(enumerate("enumerate")))
# [(0, 'e'), (1, 'n'), (2, 'u'), (3, 'm'), (4, 'e'), (5, 'r'), (6, 'a'), (7, 't'), (8, 'e')]
# or
print([i for i in enumerate("enumerate")])
# or
print(*enumerate("enumerate"))
# or
for i in enumerate("enumerate"):
    print(i)
# or
for k, v in enumerate("enumerate", 1):
    print("{} {}".format(k, v))

# exit # exit the running program
print("exit()")

# help
print("help()")
print(help(dir))
# Help on built-in function dir in module builtins:
#
# dir(...)
#     dir([object]) -> list of strings
#
#     If called without an argument, return the names in the current scope.
#     Else, return an alphabetized list of names comprising (some of) the attributes
#     of the given object, and of attributes reachable from it.
#     If the object supplies a method named __dir__, it will be used; otherwise
#     the default dir() logic is used and returns:
#       for a module object: the module's attributes.
#       for a class object:  its attributes, and recursively the attributes
#         of its bases.
#       for any other object: its attributes, its class's attributes, and
#         recursively the attributes of its class's base classes.

# id
print("id()")

a = 50
id(a)  # 505494576

python = "Python"
id(python)  # 14461728

# input
print("input()")

# name = input("Your Name?")


# format
print("format()")

"{} programmin language".format("Python")
'{:.2f}'.format(12)  # '12.00'
format(12, '.2f')  # ‘12.00’

# filter
print("filter()")
l1 = [400, 176, 64, 175, 355, 13, 207, 298, 397, 386, 31, 120, 120, 236, 241, 123, 249, 364, 292, 153]

# 1
for i in l:
    if i % 2 == 1:
        print(i)

# 2
[i for i in l1 if i % 2 == 1]


#############################
# filter sample
def odd(number):
    return number % 2 == 1


print(odd(11))  # True
print(odd(12))  # False
print(filter(odd, l1))  # <filter object at 0x7f69eea53a00>
# 1
print(list(filter(odd, l1)))  # [175, 355, 13, 207, 397, 31, 241, 123, 249, 153]

# or
# 2
print(*filter(odd, l1))  # 175 355 13 207 397 31 241 123 249 153
# or
# 3
print([i for i in filter(odd, l1)])  # [175, 355, 13, 207, 397, 31, 241, 123, 249, 153]


# filter sample 2
def grade_system(n):
    if n in range(0, 50): return 'F'
    if n in range(50, 70): return 'D'
    if n in range(70, 80): return 'C'
    if n in range(80, 90): return 'B'
    if n in range(90, 101): return 'A'


grades = {'Ahmet': 60,
          'Sinan': 50,
          'Mehmet': 45,
          'Ceren': 87,
          'Selen': 99,
          'Cem': 98,
          'Can': 51,
          'Kezban': 100,
          'Hakan': 66,
          'Mahmut': 80}


def filter_70(n):
    return n >= 70


print(*filter(filter_70, grades.values()))  # 87 99 98 100 80

#############################
# hash
print("hash()")
print(hash(1))  # 1
print(hash(True))  # 1
print(hash("python"))  # 8610676743445480263

# isinstance
print("isinstance()")
print(type("python"))  # <class 'str'>
print(isinstance("python", str))  # True
print(isinstance("python", set))  # False

# len
print("len()")
# print(len(0))
# print(len(True))
print(len("python"))  # 6
print(len([1, 2, 3, 4, 5]))  # 5

# map
print("map()")
l = [1, 4, 5, 4, 2, 9, 10]

# square
for i in l:
    i ** 2


####################
def square(n):
    return n ** 2


print(map(square, l))  # <map object at 0x7f766c65b880>
print(list(map(square, l)))  # [1, 16, 25, 16, 4, 81, 100]

# max min
print("max() min()")
print(max(1, 2, 3))  # 3
print(max([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))  # 9
print(max(["python", "programming", "language"], key=len))  # programming

# max sample
languages = {"python": "a", "java": "b", "javascript": "c", "csharp": "d", "c": "e"}


def top_lang(n):
    d = {"a": 0, "b": 1, "c": 3, "d": 4, "e": 5}
    return d[n]


print(max(languages.values(), key=top_lang))
######
print(min(1, 2, 3))  # 1
print(min([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))  # 0

# open file operations
print("open()")

open("01_print_file.py", mode='r', buffering=-1, encoding=None,
     errors=None, newline=None, closefd=True, opener=None)

import io

print(io.DEFAULT_BUFFER_SIZE)  # 8192

f = open('01_print_file.py', encoding='utf-8', errors="ignore")

# pow (2**3)
print("pow()")
print(pow(2, 3))  # (2*2*2) = 8
pow(2, 3, 2)  # (2*2*2) % 2 = 0, (2 ** 3) % 2 modülüs

# print
print("print()")  #:)

# print(deg1, deg2, deg3, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

# quit
print("quit()")
# exit program

# range
print("range()")
for r in range(10):
    print(r)

l = range(0, 10)
print(l)  # range(0, 10)
print(list(l))
print(tuple(l))
print(set(l))
print(frozenset(l))
print(*l, sep=",")

print([r for r in range(0, 20, 3)])  # [0, 3, 6, 9, 12, 15, 18]

# reversed
print("reversed()")
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(*reversed(l))
# or
l[::-1]

# sorted
print("sorted()")
l = [1, 5, 3, 7, 0, 1, 3, 5, 1]
print(*sorted(l))
# or
print(sorted("python"))

# TR language sorted
import locale

# locale.setlocale(locale.LC_ALL, 'tr_TR')  # GNU/Linux
# locale.setlocale(locale.LC_ALL, 'Turkish_Turkey.1254')  # Windows

# print(*sorted("CEVHERİ"), key=locale.strxfrm)

chars = "abcçdefgğhıijklmnoöprsştuüvyz"
translate = {'a': 0, 'b': 1, 'c': 2, 'ç': 3, 'd': 4,
             'e': 5, 'f': 6, 'g': 7, 'ğ': 8, 'h': 9,
             'ı': 10, 'i': 11, 'j': 12, 'k': 13,
             'l': 14, 'm': 15, 'n': 16, 'o': 17,
             'ö': 18, 'p': 19, 'r': 20, 's': 21,
             'ş': 22, 't': 23, 'u': 24, 'ü': 25,
             'v': 26, 'y': 27, 'z': 28}
# or
translate = {i: chars.index(i) for i in chars}
# !!!!!!!
l = ["i", "a", "ş", "ü", "ç"]
print(*sorted(l, key=lambda x: translate.get(x[0])))


def tr_sorted(word):
    return [translate.get(word[i]) for i in range(len(word))]


print(*sorted(l, key=tr_sorted), sep="\n")

# --------------------------------------------

elements = [('ahmet', 33, 'karataş'),
            ('mehmet', 45, 'arpaçbahşiş'),
            ('sevda', 24, 'arsuz'),
            ('arzu', 40, 'siverek'),
            ('abdullah', 30, 'payas'),
            ('ilknur', 40, 'kilis'),
            ('abdurrezzak', 40, 'bolvadin')]

print(*sorted(elements), sep="\n")
print()


def custom_sort2(l):
    return l[1]


print(*sorted(elements, key=custom_sort2), sep="\n")

print()


def custom_sort3(l):
    return (l[1], l[2])


print(*sorted(elements, key=custom_sort3), sep="\n")
# TR sorted istihza.com example
# https://web.archive.org/web/20161017211231/www.istihza.com/forum/viewtopic.php?f=25&t=1523
# harfler = 'abcçdefgğhıijklmnoöprsştuüvyz'
# çevrim = {i: harfler.index(i) for i in harfler}
#
# def sırala(kelime):
#     return ([çevrim.get(kelime[i]) for i in range(len(kelime))])
#
# isimler = ['ahmet', 'can', 'iskender', 'cigdem',
#            'ismet', 'ismail', 'ismit', 'çiğdem',
#            'ismıt', 'ışık', 'şule']
#
# print(*sorted(isimler, key=sırala), sep='\n')

# slice
print("slice()")
l = ["python", "programming", "language"]

print(l[::])  # all
print(l[1::])
print(l[:2:])
print(l[::2])

print("slice(start, stop, step")

sl = slice(0, 2)
print(l[sl])

# sum
print("sum()")
l = [1, 2, 3, 4]
print(sum(l))  # 10

print(sum(l, 10))  # 20

# type
print("type()")
print(type(0))
print(type(True))
print(type(""))
print(type([]))
print(type(()))
print(type(set()))
print(type({}))

# zip
print("zip()")
a1 = ['a', 'b', 'c']
a2 = ['d', 'e', 'f']

print(*zip(a1, a2))
for a, b in zip(a1, a2):
    print(a, b)

# vars() === locals()
# vars(str) === dir(str)
print("vars()")

# print(locals())
print(vars())

print(vars(str))
print()
print(vars(dict))


# and more
# memoryview
# iter
# next
# object
# property
# staticmethod
# super
# getattr
# hasattr
# delattr
# classmethod
# issubclass
# setattr
# __import__