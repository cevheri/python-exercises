# packages
# ref : https://pypi.org


# package install
# pip3 install paket_adı
# pip3 install sphinx win
# sudo pip3 install sphinx linux

# django
# https://github.com/django/django/archive/master.tar.gz
# https://www.djangoproject.com
# tar.gz open
# cd django-master
# python3 setup.py install
# import django


import urllib

import urllib.request

#

dir(urllib)
# ['__builtins__', '__cached__', '__doc__', '__file__',
#  '__loader__', '__name__', '__package__', '__path__', '__spec__']

print(urllib.__path__)
# ['/home/cevher/anaconda3/envs/python-exercises/lib/python3.8/urllib']

from urllib import request
# urllib.request.urlopen('https://www.djangoproject.com')

from urllib.request import urlopen

request.urlopen('https://www.djangoproject.com')

# + directory                 # package
# |___module1.py
# |___module2.py
# |___module3.py
#     + subdirectory
#     |___submodule1.py
#     |___submodule2.py
##############################
# add path
# import os, sys
# user = os.environ['HOME'] #for windows os.environ['HOMEPATH']
# desktop = os.path.join(user, 'Desktop')
# sys.path.append(desktop)
#
#
#
