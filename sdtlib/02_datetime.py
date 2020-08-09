# datetime module
# 1- date
# 2- time
# 3- datetime

from datetime import datetime, timedelta
import locale

# locale - a
locale.setlocale(locale.LC_ALL, "tr_TR.UTF-8")

dir(datetime)

"""['__add__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__',
'__forma t__', '__ge__', '__getattribute__', '__gt__', '__hash__',
'__init__', '__le__', '__lt__', '__ne__', '__new__', '__radd__',
'__reduce__', '__reduce_ex__', '__rep r__', '__rsub__', '__setattr__',
'__sizeof__', '__str__', '__sub__', '__subclass hook__', 'astimezone',
'combine', 'ctime', 'date', 'day', 'dst', 'fromordinal', 'fromtimestamp',
'hour', 'isocalendar', 'isoformat', 'isoweekday', 'max', 'microsecond',
'min', 'minute', 'month', 'now', 'replace', 'resolution', 'second',
'strftime', 'strptime', 'time', 'timestamp', 'timetuple', 'timetz', 'today',
'toord inal', 'tzinfo', 'tzname', 'utcfromtimestamp', 'utcnow', 'utcoffset',
'utctimetuple', 'weekday', 'year']
"""
print()
print("now() and today()")
now = datetime.now()
today = datetime.today()
print(now)

print(now.year)
print(now.month)
print(now.day)

print(now.hour)
print(now.minute)
print(now.second)

print(now.microsecond)

#######################
print()
print("ctime")
print(datetime.ctime(today))  # Sat Aug  8 04:19:51 2020

#######################
print()
print("strftime")

print(datetime.strftime(today, '%c'))  # Sat Aug  8 04:21:13 2020
print(datetime.strftime(today, '%Y'))  # 2020
"""
%a hafta gününün kısaltılmış adı
%A hafta gününün tam adı
%b ayın kısaltılmış adı
%B ayın tam adı
%c tam tarih, saat ve zaman bilgisi
%d sayı değerli bir karakter dizisi olarak gün
%j belli bir tarihin, yılın kaçıncı gününe denk geldiğini gösteren 1-366 arası bir sayı
%m sayı değerli bir karakter dizisi olarak ay
%U belli bir tarihin yılın kaçıncı haftasına geldiğini gösteren 0-53 arası bir sayı
%y yılın son iki rakamı
%Y yılın dört haneli tam hali
%x tam tarih bilgisi
%X tam saat bilgisi
"""

print(datetime.strftime(today, '%B'))
print(datetime.strftime(today, '%d %B %Y'))  # 08 Ağustos 2020

#######################
print()
print("strptime")

t = '27 Mayıs 2014'
day, month, year = t.split()

t = '27 Mayıs 2014 saat 12:34:44'
day, month, year, hour = [i for i in t.split() if "saat" not in i]
print(day, month, year, hour)  # 27 Mayıs 2014 12:34:44

z = datetime.strptime(t, '%d %B %Y saat %H:%M:%S')
# datetime(2014, 5, 27, 0, 34, 44)

#######################
print()
print("fromtimestamp")
import os

c_timestamp = os.stat("01_regular_expressions.py").st_mtime
print(c_timestamp)  # 1596831901.5432215
d = datetime.fromtimestamp(c_timestamp)
print(d)  # 2020-08-07 23:25:01.543221
print(datetime.strftime(d, '%c'))  # Cum 07 Ağu 2020 23:25:01

#######################
print()
print("timestamp")
ts = datetime.timestamp(today)
d = datetime.fromtimestamp(ts)

#######################
print()
print("custom date")
dt = datetime(2007, 6, 1, 10, 00, 00, 5)
timedelta1 = today - dt
print(timedelta1)  # 4816 days, 18:43:06.024948
print(timedelta1.days)
print(timedelta1.seconds)
print(timedelta1.microseconds)

# + 100 days difference
timedelta2 = timedelta(days=100)


diff = timedelta(days=200)
past = today - diff
print(past)