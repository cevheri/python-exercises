# list

list0 = []

list1 = ["e1", "e2", "e3"]
print(list1)  # ['e1', 'e2', 'e3']
print(type(list1))  # <class 'list'>

list2 = ["element", 2, 3.1, True]
print(list2)  # ['element', 2, 3.1, True]
print(list2[2])  # 3.1

list3 = ["l1_element_1", ["l2_element_1", "l2_element_2"]]
print(list3[1][0])  # l2_element_1

list4 = dir(str)
# ['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__',
# '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__',
# '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__',
# '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__',
# '__subclasshook__', 'capitalize', 'center', 'count', 'encode', 'endswith',
# 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha',
# 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable',
# 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip',
# 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition',
# 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase',
# 'title', 'translate', 'upper', 'zfill']

print(list4[0])  # __add__

val = "Python Programming Language"
list5 = val.split()
print(list5)  # ['Python', 'Programming', 'Language']

# example
numbers = [[0, 10], [6, 60], [12, 54], [67, 99]]
for r in numbers:
    print(*range(*r))
# 0 1 2 3 4 5 6 7 8 9
# 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59
# 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53
# 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98


# list method
alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
list6 = list(alphabet)
print(
    list6)  # ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v', 'y', 'z']

list7 = list()

print(range(10))  # range(0, 10)
for r in range(10):
    print(r, end=",")
# 0,1,2,3,4,5,6,7,8,9,
print()
print(*range(10))  # 0 1 2 3 4 5 6 7 8 9
print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# modify list
list8 = list(range(10))
print(list8)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list8[0] = 11
print(list8)  # [11, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# example
list9 = [1, 2, 3]
list9 = [4, 5, 6]
list9[0:3] = 7, 8, 9
list9[0:len(list9)] = 10, 11, 12
list9[:] = 13, 14, 15

# add list
list10 = [1, 2, 3]
list10 + [4]

# merge list
list11 = [1, 2, 3]
list12 = [4, 5, 6]
list13 = list11 + list12

# delete element list
print(list13)  # [1, 2, 3, 4, 5, 6]
del list13[0]
print(list13)  # [2, 3, 4, 5, 6]

# complete delete list
del list13

# copy and change list
list14 = [1, 2, 3]
list15 = list14

print(list14)  # [1, 2, 3]
print(list15)  # [1, 2, 3]

list14[0] = 9
print(list14)  # [1, 2, 3]
print(list15)  # [1, 2, 3]

print(id(list14))
print(id(list15))
# ids equals

list16 = list14[:]
print(id(list14))
print(id(list16))
# ids not equals

list17 = list(list14)
print(id(list14))
print(id(list17))
# ids not equals

# “List Comprehension”
l1 = list(range(10))
print(l1)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

l2 = []
for i in range(10):
    l2 += [i]
print(l2)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# alternative
l3 = [i for i in range(10)]
print(l3)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

l4 = [i for i in range(10) if i % 2 == 0]
print(l4)  # [0, 2, 4, 6, 8]

# example convert [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
l5 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9],
      [10, 11, 12]]

l6 = []
for i in l5:
    for z in i:
        l6 += [z]
print(l6)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# alternative
l7 = [z for i in l5 for z in i]
print(l7)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]


liste1 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9],
          [10, 11, 12],
          [13, 14, 15],
          [16, 17, 18],
          [19, 20, 21],
          [22, 23, 24],
          [25, 26, 27],
          [28, 29, 30],
          [31, 32, 33]]


liste2 = [1, 27, 88, 98, 50, 9, 28, 45, 54, 66, 61, 23, 10, 33,
          22, 12, 6, 99, 63, 26, 87, 25, 77, 5, 16, 93, 99, 44,
          59, 69, 34, 10, 60, 92, 61, 44, 5, 3, 23, 99, 79, 51,
          89, 63, 53, 31, 76, 41, 49, 10, 88, 63, 55, 43, 40, 71,
          16, 49, 78, 41, 35, 97, 33, 76, 25, 81, 15, 99, 64, 20,
          33, 6, 89, 81, 44, 53, 59, 75, 27, 15, 64, 36, 72, 78,
          34, 36, 20, 41, 41, 75, 56, 30, 86, 46, 9, 42, 21, 64,
          26, 52, 77, 65, 64, 12, 38, 1, 35, 20, 73, 71, 37, 35,
          72, 38, 100, 52, 16, 49, 79]

for i in liste1:
    ortak = [z for z in i if z in liste2]
    if len(ortak) == len(i):
        print(i)