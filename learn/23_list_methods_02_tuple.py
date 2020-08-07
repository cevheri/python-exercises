# tuple methods
#
#    index()
#    count()


print(dir(tuple))
print([i for i in dir(tuple) if not "_" in i])
# ['count', 'index']

tp = (1,2,3,4,5,6,7,8,9,0,0,0)
print(tp.index((0))) # 9


print(tp.count(0)) # 3