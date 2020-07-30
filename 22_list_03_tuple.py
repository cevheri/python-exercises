# tuple (immutable)

tp = ()
print(type(tp))

tp = (1, 2, 3)
print(tp)

tp = (1, "str", 3.2, False)
print(tp)
# alternative
tp = 1, "str", 3.2, False
print(tp)

tp = tuple("abcde")
print(tp)

tp = tuple([1, "str", 3.2, False])
print(tp)

# !!!!!!!
tp_str = ("1")
print(type(tp_str)) # <class 'str'>

tp = ("1",)
# or
tp = "1",
print(type(tp)) # <class 'tuple'>

####
print(tp[0]) # 1
