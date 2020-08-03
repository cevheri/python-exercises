# sets

blank_set = set()

print(type(blank_set))  # <class 'set'>

s1 = set([1, 2, 3, 4, 5])

l = [1, 2, 3, 4, 5]
t = (1, 2, 3, 4, 5)
c = "Python"
d = {"1": "a", "2": "b"}

s1 = set(l)
s2 = set(t)
s3 = set(c)
s4 = set(d)
print(s1)
print(s2)
print(s3)
print(s4)

##
s5 = {"a", "b", "c", "d"}
print(type(s5))  # <class 'set'>
print(s5)

#
l2 = [(key, val) for key, val in d.items()]
s6 = set(l2)
print(s6)

#  (Set Comprehensions)
# list
print("random")
import random

l = [random.randint(0, 10) for i in range(10)]
l2 = [i for i in l if i < 8]
print(l2)

# set
s7 = {i for i in l if i < 8}
print(s7)

s8 = {i for i in l if i < 8}
print(s8)

# set methods
print(dir(set))
for i in dir(set):
    if "__" not in i:
        print(i)

# add :)
# clear :)
# copy :)
# difference
# difference_update
# discard
# intersection
# intersection_update
# isdisjoint
# issubset
# issuperset
# pop
# remove
# symmetric_difference
# symmetric_difference_update
# union
# update
##########################
print('-' * 30)
# difference()
print("difference()")
s1 = set([1, 2, 3, 4, 5])
s2 = set([1, 6, 7, 8, 9])

print(s1.difference(s2))  # {2, 3, 4, 5}
print(s2.difference(s1))  # {8, 9, 6, 7}
# or
s1 - s2
s2 - s1

print('-' * 30)
# difference_update()
print("difference_update()")
s1 = set([1, 2, 3, 4, 5])
s2 = set([1, 2, 7, 8, 9])
s1.difference_update(s2)
print(s1)  # {3, 4, 5}

print('-' * 30)
# discard() or remove()
# delete element
print("discard() or remove()")
s2.discard(9)  #
s2.remove(1)

print('-' * 30)
# intersection()
print("intersection()")
s1 = set([1, 2, 3, 4, 5])
s2 = set([1, 2, 7, 8, 9])

print(s1.intersection(s2))  # {1, 2}
# or
print(s1 & s2)  # {1, 2}

print('-' * 30)
# intersection_update()
print("intersection_update()")
s1 = set([1, 2, 3, 4, 5])
s2 = set([1, 2, 7, 8, 9])
s1.intersection_update(s2)
print(s1)  # {1, 2}

print('-' * 30)
# isdisjoint()
print("isdisjoint()")
s1 = set([1, 2, 3, 4, 5])
s2 = set([1, 2, 7, 8, 9])
print(s1.isdisjoint(s2))  # False

print('-' * 30)
# issubset()
print("issubset()")
s1 = set([1, 2])
s2 = set([1, 2, 7, 8, 9])
print(s1.issubset(s2))  # True
print(s2.issubset(s1))  # False
print('-' * 30)
# issuperset()
print("issuperset()")
s1 = set([1, 2])
s2 = set([1, 2, 7, 8, 9])
print(s1.issuperset(s2))  # False
print(s2.issuperset(s1))  # True
print('-' * 30)
# union()
print("union()")
s1 = set([1, 2])
s2 = set([1, 2, 7, 8, 9])
print(s1.union(s2))  # {1, 2, 7, 8, 9}
# or
print(s1 | s2)  # {1, 2, 7, 8, 9}

print('-' * 30)
# update()
print("update()")
s = set([1, 2, 3, 4, 5])
l = ["a", "b", "c"]
for i in l:
    s.add(i)
# or
s.update(l)
print(s)  # {'c', 1, 2, 3, 4, 5, 'b', 'a'}

print('-' * 30)
# symmetric_difference()
print("symmetric_difference()")
s1 = set([1, 2, 3, 4, 5])
s2 = set([1, 2, 7, 8, 9])
print(s1.difference(s2))  # {3, 4, 5}
print(s2.difference(s1))  # {8, 9, 7}
print(s1.symmetric_difference(s2)) # {3, 4, 5, 7, 8, 9}

print('-' * 30)
# symmetric_difference_update()
print("symmetric_difference_update()")
s1 = set([1, 2, 3, 4, 5])
s2 = set([1, 2, 7, 8, 9])
s1.symmetric_difference_update(s2)
print(s1)  # {3, 4, 5, 7, 8, 9}

print('-' * 30)
# pop()
# random delete and print
print("pop()")
s1 = set([1, 2, 3, 4, 5])
print(s1.pop()) # 1
#
#

#######################################################
# frozenset
# 'copy', 'difference', 'intersection',
# 'isdisjoint', 'issubset', 'issuperset',
# 'symmetric_difference', 'union'

fs = frozenset([1, 2, 3, 4, 5])
