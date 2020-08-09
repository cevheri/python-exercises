# timeit module
# timeit — Measure execution time of small code snippets
# https://docs.python.org/3.5/library/timeit.html
# https://github.com/python/cpython/blob/3.5/Lib/timeit.py

# Tool for measuring execution time of small code snippets.
# This module avoids a number of common traps for measuring execution times.


import timeit

t1 = timeit.timeit('"-".join(str(n) for n in range(100))', number=100)
print(t1)
# 0.0475664269997651
t2 = timeit.timeit('"-".join([str(n) for n in range(100)])', number=1000)
print(t2)
# 0.21502946299915493
t3 = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(t3)
# 1.786532415999318


timeit.Timer("for i in range(10): oct(i)", "gc.enable()").timeit()

timeit.repeat("for i in range(10): oct(i)", "gc.enable()", repeat=3, number=1000000)

# print_exc(file)
t = timeit.Timer()
try:
    t.timeit()
    # t.repeat(...)
except Exception:
    t.print_exc()

##########################################################
# terminal - command window
# python3 -m timeit '"-".join(str(n) for n in range(100))'
# 10000 loops, best of 3: 29 usec per loop
#
# python3 -m timeit '"-".join([str(n) for n in range(100)])'
# 10000 loops, best of 3: 25.3 usec per loop
#
# python3 -m timeit '"-".join(map(str, range(100)))'
# 10000 loops, best of 3: 20 usec per loop
####################
# python -m timeit 'try:' '  str.__bool__' 'except AttributeError:' '  pass'
# 1000000 loops, best of 3: 0.99 usec per loop
#
# python -m timeit 'if hasattr(str, "__bool__"): pass'
# 1000000 loops, best of 3: 0.476 usec per loop
#
# python -m timeit 'try:' '  int.__bool__' 'except AttributeError:' '  pass'
# 1000000 loops, best of 3: 0.966 usec per loop
#
# python -m timeit 'if hasattr(int, "__bool__"): pass'
# 1000000 loops, best of 3: 0.479 usec per loop
#############################################################3
## try, hasattr()
import timeit

s = """\
try:
    str.__bool__
except AttributeError:
    pass
"""

timeit.timeit(stmt=s, number=100000)
# 0.08558237599936547

s = "if hasattr(str, '__bool__'): pass"
timeit.timeit(stmt=s, number=100000)
# 0.0541383109994058


s = """\
try:
    int.__bool__
except AttributeError:
    pass
"""

timeit.timeit(stmt=s, number=100000)
# 0.011753970000427216

s = "if hasattr(int, '__bool__'): pass"
timeit.timeit(stmt=s, number=100000)


# 0.016129147999890847
######################################################

def test():
    L = [i for i in range(100)]

    # if __name__ == '__main__': # call current module


import timeit

print(timeit.timeit("test()",
                    setup="from __main__ import test"))


#    4.163065000997449
###################################################
# globals
def f(x):
    return x ** 2


def g(x):
    return x ** 4


def h(x):
    return x ** 8


import timeit

print(timeit.timeit('[func(42) for func in (f,g,h)]',
                    globals=globals()))
# 1.632076413003233
##########################################################
# codes that do similar things
# in terminal
# python -m timeit '"a" + "b"'
# 100000000 loops, best of 3: 0.0183 usec per loop
#
# python -m timeit '"{}.{}".format("a", "b")'
# 1000000 loops, best of 3: 0.215 usec per loop
#
# python -m timeit '"%s%s" %("a", "b")'
# 10000000 loops, best of 3: 0.117 usec per loop
#
# python -m timeit '"".join(("a", "b"))'
# 10000000 loops, best of 3: 0.109 usec per loop
#####
##
# in python
import timeit

timeit.timeit('"a" + "b"', number=1000000)
# 0.018340642998737167

timeit.timeit('"{}{}".format("a", "b")', number=1000000)
# 0.3770097929991607

timeit.timeit('"%s%s" %("a", "b")', number=1000000)
# 0.2078534940010286

timeit.timeit('"".join(("a", "b"))', number=1000000)
# 0.1585119779992965
