# list methods
print(dir(list))
# dir([])

# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__',
#  '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
#  '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__',
#  '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__',
#  '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__',
#  '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
#  'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop',
#  'remove', 'reverse', 'sort']

print([i for i in dir(list) if not "_" in i])

# ['append', 'clear', 'copy', 'count', 'extend', 'index',
#  'insert', 'pop', 'remove', 'reverse', 'sort']

# append()
ls = [1, 2, 3, 4]
print(ls)  # [1, 2, 3, 4]
ls.append(5)
print(ls)  # [1, 2, 3, 4, 5]
ls = ls + [6]
print(ls)  # [1, 2, 3, 4, 5, 6]

# extend()
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l1.extend(l2)
print(l1)  # [1, 2, 3, 4, 5, 6]

# insert()
l1.insert(0, 0)
print(l1)  # [0, 1, 2, 3, 4, 5, 6]

# remove()
l1.remove(0)
print(l1)  # [1, 2, 3, 4, 5, 6]

# pop()
l1.pop()
l1.pop(0)

# reverse()
l1.reverse()
print(l1)  # [6, 5, 4, 3, 2, 1]
# or
print(l1[::-1])  # [1, 2, 3, 4, 5, 6]
# or
print(reversed(l1))  # <list_reverseiterator object at 0x7f8cb68bd910>
print(*reversed(l1))  # 1 2 3 4 5 6
print(list(reversed(l1)))  # [1, 2, 3, 4, 5, 6]

# sort()
ls = [6, 5, 3, 4, 1, 2, 9, 0]
print(ls)  # [6, 5, 3, 4, 1, 2, 9, 0]
ls.sort()
print(ls)  # [0, 1, 2, 3, 4, 5, 6, 9]
ls.sort(reverse=True)
print(ls)  # [9, 6, 5, 4, 3, 2, 1, 0]

# example tr language sort
alphabet = "abcçdefgğhıijklmnoöprsştuüvyz"
translate = {a: alphabet.index(a) for a in alphabet}
names = ["ahmet", "ışık", "ismail", "çiğdem", "can", "şule"]
names.sort(key=lambda x: translate.get(x[0]))
print(names)

# index()
print(l1)  # [5, 4, 3, 2]
print(l1.index(5))  # 0

# count()
print(l1.count(4))  # 1

# copy()
l2 = l1.copy()

# clear()
l1.clear() # []
