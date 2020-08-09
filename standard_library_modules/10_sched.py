# sched — Event scheduler
# The scheduler class defines a generic interface to scheduling events.
# It needs two functions to actually deal with the “outside world” — timefunc
# should be callable without arguments, and return a number (the “time”, in any units whatsoever).
# The delayfunc function should be callable with one argument,
# compatible with the output of timefunc, and should delay that many time units.
# delayfunc will also be called with the argument 0 after each event is
# run to allow other threads an opportunity to run in multi-threaded applications.
# ref : https://docs.python.org/3/library/sched.html


# example

import sched, time

s = sched.scheduler(time.time, time.sleep)


def print_time(a='default'):
    print("From print_time", time.time(), a)


def print_some_times():
    print(time.time())
    s.enter(10, 1, print_time)
    s.enter(5, 2, print_time, argument=('positional',))
    s.enter(5, 1, print_time, kwargs={'a': 'keyword'})
    s.run()
    print(time.time())


print_some_times()
###########################################################

s=sched.scheduler(time.time,time.sleep)
def zamanı_yazdır(sıra):
    print(f"Zaman: {time.time()} ,{sıra}")

def farklı_zamanları_yazdır():
    print(time.time())
    s.enter(10,1,zamanı_yazdır,argument=("Birinci",))
    s.enter(5,1,zamanı_yazdır,argument=("İkinci",))
    s.enter(5,2,zamanı_yazdır,argument=("Üçüncü",))
    s.enter(5,1,zamanı_yazdır,argument=("Dördüncü",))
    s.run()
    print(time.time())

farklı_zamanları_yazdır()




s=sched.scheduler(time.time,time.sleep)
yazdırılacak_değer="Merhaba Dünya"
def değiştir():
    global yazdırılacak_değer
    yazdırılacak_değer="Merhaba Zalim Dünya"

def yazdır():
    print(yazdırılacak_değer)

suan=time.time()
if(s.empty()):
    s.enterabs(suan+5,1,yazdır)
    s.enterabs(suan+6,2,değiştir)
    s.enterabs(suan+6,1,yazdır)
    s.enter(10,1,yazdır)
s.run()


import sched,time
s=sched.scheduler(time.time,time.sleep)
suan=time.time()
def çıktı():
    global suan
    suan+=2
    print(suan)
    s.enterabs(suan,1,çıktı)

s.enter(5,1,çıktı)
s.run()
