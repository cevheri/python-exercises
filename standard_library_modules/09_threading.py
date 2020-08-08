# threading module
# source code :
# https://github.com/python/cpython/blob/3.8/Lib/threading.py
# https://hg.python.org/cpython/file/3.5/Lib/threading.py
"""Thread module emulating a subset of Java's threading model."""

# ref : https://docs.python.org/3.8/library/threading.html

# Note regarding PEP 8 compliant names
#  This threading model was originally inspired by Java, and inherited
# the convention of camelCase function and method names from that
# language. Those original names are not in any imminent danger of
# being deprecated (even for Py3k),so this module provides them as an
# alias for the PEP 8 compliant names
# Note that using the new PEP 8 compliant names facilitates substitution
# with the multiprocessing module, which doesn't provide the old
# Java inspired names.

import threading
import time


# local_thread= threading.local()
# local_thread.x = 1


def hello():
    print("hello, world")


t = threading.Timer(1.0, hello)
t.start()

time.sleep(2)


##########################################
# /usr/bin/env python3
# -*- coding: utf-8 -*-

def target_function():
    print("do something")


for i in range(4):
    t = threading.Thread(target=target_function())
    t.start()


#####################################################
# /usr/bin/env python3
# -*- coding: utf-8 -*-

def target_function_2(param):
    print("do something : {}".format(param))


for i in range(4):
    t = threading.Thread(target=target_function_2, args=(i,))
    t.start()
time.sleep(1)


##########################################################

# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def f():
    print(threading.currentThread().getName(), "Starting")
    time.sleep(1)
    print(threading.currentThread().getName(), "Ending")


def g():
    print(threading.currentThread().getName(), "Starting")
    time.sleep(1)
    print(threading.currentThread().getName(), "Ending")


t1 = threading.Thread(name="First Service", target=f)
t2 = threading.Thread(name="Second Service", target=g)
t3 = threading.Thread(target=f)
t4 = threading.Thread(target=g)

t1.start()
t2.start()
t3.start()
t4.start()

########################################################33
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# try:
#     import Tkinter as tk
# except ImportError:
#     import tkinter as tk
# import threading
#
# root = tk.Tk()
# entry = tk.Entry(master=root)
# entry.grid(row=0, column=0)
#
#
# def f():
#     button = tk.Button(master=root, text="Button")
#     while True:
#         if entry.get() == "":
#             button.grid_forget()
#         else:
#             button.grid(row=1, column=0)
#
#
# t1 = threading.Thread(target=f)
# t1.daemon = True
# t1.start()
# t1.join(1)
# root.mainloop()
time.sleep(3)


#########################################################33
#
#
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

def f():
    print("f fonksiyonu")


def g():
    print("g fonksiyonu")


def h():
    print("h fonksiyonu")


t1 = threading.Thread(target=f)
t2 = threading.Thread(target=g)
t3 = threading.Thread(target=h)

lock = threading.Lock()
lock.acquire()

t1.start()
lock.acquire(blocking=True, timeout=3)

t2.start()
lock.acquire(blocking=True, timeout=1)

t3.start()

#######################################
# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading


class Thread(threading.Thread):
    def __init__(self, lock):
        threading.Thread.__init__(self)
        self.lock = lock

    def run(self):
        self.lock.acquire()
        print("{} kilidi edindi.".format(self.name))
        # self.lock.acquire(blocking=True, timeout=3)
        self.lock.release()
        print("{} kilidi serbest bıraktı.".format(self.name))


__lock__ = threading.Lock()
t1 = Thread(lock=__lock__)
t2 = Thread(lock=__lock__)
t1.start()
t2.start()

###################################################3

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading


class Thread(threading.Thread):
    def __init__(self, lock):
        threading.Thread.__init__(self)
        self.lock = lock

    def run(self):
        self.lock.acquire(blocking=True, timeout=3)
        print("{} çalışıyor.".format(self.name))
        self.lock.acquire(blocking=True, timeout=1)
        print("{} çalışması bitti.".format(self.name))


__lock__ = threading.RLock()
t1 = Thread(lock=__lock__)
t2 = Thread(lock=__lock__)
t1.start()
t2.start()
#####################################################

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import threading


class Uretici(threading.Thread):
    def __init__(self, event, liste):
        threading.Thread.__init__(self)
        self.event = event
        self.liste = liste

    def run(self):
        count = 1
        while count < 10:
            self.liste.append(count)
            print("{} listeye {} tarafından eklendi."
                  .format(count, self.name))
            self.event.set()
            print("event {} tarafından ayarlandı.".format(self.name))
            self.event.clear()
            print("event {} tarafından temizlendi.".format(self.name))
            count += 1
            time.sleep(0.5)


class Tuketici(threading.Thread):
    def __init__(self, event, liste):
        threading.Thread.__init__(self)
        self.event = event
        self.liste = liste

    def run(self):
        while True:
            if self.liste:
                sayi = self.liste.pop()
                print("{}, {} tarafından listeden düşürüldü."
                      .format(sayi, self.name))
            self.event.wait()


__event__ = threading.Event()
__liste__ = []
t1 = Uretici(event=__event__, liste=__liste__)
t2 = Tuketici(event=__event__, liste=__liste__)
t1.start()
t2.start()