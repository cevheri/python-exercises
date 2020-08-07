# moduls
# examples
"""
sys
os
keyword
random
unicodedata
locale
"""

# The Python Standard Library
# https://docs.python.org/3/library/

import os

print(os.name)  # posix

# create directory
# os.makedirs("data")

print(os.getcwd())  # /home/cevher/projects/python-projects/python-exercises
print(os.listdir())
#
import sys

print(sys.version)
# 3.8.3 (default, Jul  2 2020, 16:21:59)
# [GCC 7.3.0]

import subprocess
# subprocess.call("idea")

import subprocess as sp
# sp.call("vi")
#########################
import webbrowser as wb
# wb.open("https://www.python.org/")

#
#
from os import name

print(name)
from os import path as pt

print(pt)

version = 1

from sys import *  # risk !!!

version
print(version)  # 3.8.......
# or
__all__ = ['name', 'version', 'version_info']

from sys import *

import os as oss

print(dir(oss))
# oss.__file__

# wb.__file__

import importlib

importlib.reload(sys)

# '/home/cevher/anaconda3/envs/python-exercises/lib/python3.8/
from distutils import sysconfig

print(sysconfig.get_python_lib())
# /home/cevher/anaconda3/envs/python-exercises/lib/python3.8/site-packages
# bad
sys.path.append(r'/home/cevher/projects/python-projects/custom_modules')

# good
sys.path.insert(0, r'/home/cevher/projects/python-projects/custom_modules')

print(sysconfig.get_python_lib())

# import "./custom_modules/dictionary.py"

# install module
# for https://pypi.python.org/pypi
# pip3 install module_name
# pip3 install django
# or
# python3 setup.py install

# commen property for moduls
import os, sys, random

set_os = set(dir(os))
set_sys = set(dir(sys))
set_random = set(dir(random))
print(set_os & set_sys & set_random)
# {'__doc__', '__spec__', '__name__', '__loader__', '__package__'}
##
# example import module
modules = ["os", "sys", "random", "webbrowser", "subprocess"]


def find_intersec(modules):
    sets = [set(dir(__import__(module))) for module in modules]
    return set.intersection(*sets)


print(find_intersec((modules)))
# {'__doc__', '__name__', '__package__', '__loader__', '__spec__'}
print()
#
## dynamic import module
print(__import__('os').name)

#
# __doc__
print("__doc__")
print("docstring")
print()
import os

print(os.__doc__)

# or
import random

print(help(random))
print()
#
# __name__
print(__name__)  # __main__
print(os.__name__)  # os
print()
#
# __loader__   ! pkgutil
print("__loader__")
import os

loader = os.__loader__
print(dir(loader))

import webbrowser

loader = webbrowser.__loader__
source_code = loader.get_data(webbrowser.__file__)
print(source_code)
print()
#
# __spec__
print("__spec__")
import subprocess

name = subprocess.__spec__.name
origin = subprocess.__spec__.origin
print(name, origin)

print()
#
# __package__
print("__package__")

