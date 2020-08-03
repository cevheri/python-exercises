# dictionary methods

"""
keys()
values()
items()
get()
clear()
copy()
fromkeys()
pop()
popitem()
setdefault()
update()
"""

# keys()
d1 = {"a": 0,
      "b": 1,
      "c": 2,
      "d": 3}
print(d1.keys())
print(list(d1.keys()))
print(tuple(d1.keys()))
print(", ".join(d1.keys()))

# values()
print(d1.values())
print(list(d1.values()))
print(tuple(d1.values()))
print(", ".join([str(i) for i in d1.values()]))

# items()
print(d1.items())  # dict_items([('a', 0), ('b', 1), ('c', 2), ('d', 3)])
for key, val in d1.items():
    print("{} = {}".format(key, val))

# get()
query = "e"
if query not in d1:
    print("{} not found".format(query))
else:
    print(d1[query])
# or
val = d1.get(query, "Not Found")
print(val)

# clear()
d2 = {1: "a", 2: "b"}
print(d2)
d2.clear()
print(d2)

# and terminate
del d2

# copy()
d3 = d1
print(d1, d3)
# {'a': 0, 'b': 1, 'c': 2, 'd': 3}
# {'a': 0, 'b': 1, 'c': 2, 'd': 3}

d1["e"] = 4
print(d1, d3)
# {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}
# {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4}


d2 = d1.copy()
print(d1, d2)  # {'a': 0, 'b': 1, 'c': 2, 'd': 3} {'a': 0, 'b': 1, 'c': 2, 'd': 3}
d1["e"] = 4
print(d1, d2)  # {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4} {'a': 0, 'b': 1, 'c': 2, 'd': 3}

# fromkeys()

ls = [1, 2, 3, 4, 5, 6]
d4 = dict.fromkeys(ls, "0")
print(d4)  # {1: '0', 2: '0', 3: '0', 4: '0', 5: '0', 6: '0'}

# pop()
print(d1.pop("e", "Not Found"))

# popitem()
# rondom delete
d1.popitem()

# setdefault()
d1.setdefault("e", 5)
print(d1)  # {'a': 0, 'b': 1, 'c': 2, 'e': 5}
d1.setdefault("e", 6)
print(d1)  # {'a': 0, 'b': 1, 'c': 2, 'e': 5}

# update() !!!!!!
# add and update
print(d1)
print(d2)
print(d3)
print(d4)
d1.update(d4)
print(d1)