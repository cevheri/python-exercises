# time module
# This module provides various time-related functions.
# For related functionality, see also the datetime and calendar modules.
#
# Although this module is always available,
# not all functions are available on all platforms.
# Most of the functions defined in this module
# call platform C library functions with the same name.
# It may sometimes be helpful to consult
# the platform documentation,
# because the semantics of these functions varies among platforms.
# ref : https://docs.python.org/3/library/time.html

import time
import locale
locale.setlocale(locale.LC_ALL, "tr_TR.UTF-8")

print()

print(time.gmtime(0))
# time.struct_time(
# tm_year=1970,
# tm_mon=1,
# tm_mday=1,
# tm_hour=0,
# tm_min=0,
# tm_sec=0,
# tm_wday=3,
# tm_yday=1,
# tm_isdst=0)

epoch = time.gmtime(0)
epoch.tm_year

print(time.gmtime())
# time.struct_time(
# tm_year=2020,
# tm_mon=8,
# tm_mday=8,
# tm_hour=18,  wrong
# tm_min=31,
# tm_sec=15,
# tm_wday=5,
# tm_yday=221,
# tm_isdst=0)

print(time.time())
# 1596911557.781952
# today -epoch = seconds

print(time.gmtime(time.time()))
# time.struct_time(
# tm_year=2020,
# tm_mon=8,
# tm_mday=8,
# tm_hour=18,  wrong
# tm_min=31,
# tm_sec=15,
# tm_wday=5,
# tm_yday=221,
# tm_isdst=0)

ltime = time.localtime()
print(ltime.tm_hour, ltime.tm_min, ltime.tm_sec, sep=":")
# 21:35:23

# asctime
import datetime

today = datetime.datetime.now()
print(datetime.datetime.ctime(today))
#                        Sat Aug  8 21:36:50 2020
print(time.asctime())  # Sat Aug  8 21:37:12 2020

time.asctime(time.gmtime())
time.asctime(time.gmtime(0))
time.asctime(time.localtime())

# bad way
tp = (2020, 5, 27, 13, 45, 23, 0, 0, 0)
time.asctime(tp)

# strftime()
import datetime
today = datetime.datetime.now()
print(datetime.datetime.strftime(today, '%c'))
print(time.strftime('%c'))

##########
t = '27 Mayıs 2020'
date = time.strptime(t, '%d %B %Y')
print(date)
# time.struct_time(
# tm_year=2020,
# tm_mon=5,
# tm_mday=27,
# tm_hour=0,
# tm_min=0,
# tm_sec=0,
# tm_wday=2,
# tm_yday=148,
# tm_isdst=-1)

#######################################3
# sleep()
for i in range(10):
    time.sleep(.2)
    print(i, time.localtime().tm_sec)

for i in range(9, 0, -1):
    time.sleep(0.2)
    print(i, time.localtime().tm_sec)