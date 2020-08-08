# Regular Expressions
#
#
# Some people, when confronted with a problem, think “I know, I’ll use regular expressions.” Now they have two problems.
# Jamie Zawinski
#
# ref : https://docs.python.org/3/howto/regex.html
import re

print(dir(re))
# ---------------------------------------------------------------
# | ['A', 'ASCII', 'DEBUG', 'DOTALL', 'I', 'IGNORECASE',         |
# | 'L', 'LOCALE', 'M', 'MULTILINE', 'Match', 'Pattern',         |
# | 'RegexFlag', 'S', 'Scanner', 'T', 'TEMPLATE', 'U',           |
# | 'UNICODE', 'VERBOSE', 'X', '_MAXCACHE', '__all__',           |
# | '__builtins__', '__cached__', '__doc__', '__file__',         |
# | '__loader__', '__name__', '__package__', '__spec__',         |
# | '__version__', '_cache', '_compile', '_compile_repl',        |
# | '_expand', '_locale', '_pickle', '_special_chars_map',       |
# | '_subx', 'compile', 'copyreg', 'enum', 'error', 'escape',    |
# | 'findall', 'finditer', 'fullmatch', 'functools', 'match',    |
# | 'purge', 'search', 'split', 'sre_compile', 'sre_parse',      |
# | 'sub', 'subn', 'template']                                   |
# ----------------------------------------------------------------
# Match Method
print("Match Methods")
print(help(re.match))
# ----------------------------------------------------------------
# Help on function match in module re:
#
# match(pattern, string, flags=0)
#     Try to apply the pattern at
#     the start of the string, returning
#     a Match object, or None if no match was found.
# -----------------------------------------------------------------

a = "Python is a powerful programming language."

print(re.match("Python", a))  # match object
# <re.Match object; span=(0, 6), match='Python'>

print(re.match("powerful", a))  # match object
# None

print(a.split()[0] == "Python")  # True
print(a.split()[0] == "powerful")  # False
print(a.startswith("Python"))  # True

print(a[0:6])  # Python

print(re.match("Java", a))  # None
#######################################################
#
#
query = "1234567890"

print(re.match("1", query))  # <re.Match object; span=(0, 1), match='1'>
print(re.match("1234", query))  # <re.Match object; span=(0, 4), match='1234'>
print(re.match("124", query))  # None

re_match = re.match("1234", query)
print(type(re_match))  # <class 're.Match'>
print(dir(re_match))  #

if re_match:
    print(re_match.span())  # (0, 4)
    print(re_match.group())  # 1234
else:
    print("Don't match")
print()
print("-" * 30)
###################################################
#
# search() method first find text
print("search() method")

# match
print(re.match("powerful", a))  # None

# search
match = re.search("powerful", a)
print(match)  # <re.Match object; span=(12, 20), match='powerful'>
if match:
    print(match.span())  # (12, 20)
    print(match.group())
else:
    print("Don't match")

# list search
l = a.split()
for i in l:
    m = re.search("Python", i)
    if m:
        print(m.span())
        print(m.group())

# serch web site
import urllib
from urllib.request import urlopen

f = urlopen("https://www.djangoproject.com/")
for i in f:
    m = re.search(b"Get started with Django", i)
    # m1 = re.search(b"Django", i)
    if m:
        print(m.span())
        print(m.group())
# (67, 90)
# b'Get started with Django'
print()
#
f1 = urlopen("https://www.djangoproject.com/")
data = str(f1.read())
match = re.search("Django", data)
if match:
    print(match.span())
else:
    print("Don't match")
# (348, 354)
print()
print("-" * 30)
#################################################
#
# findall() method
print("findall() method")
f1 = urlopen("https://www.djangoproject.com/")
data = str(f1.read())
match = re.findall("Django", data)  # ['Django', 'Django', .....
print(match)
print()
print("-" * 30)
#################################################
#
# Metacharacters
# [ ] . \* + ? { } ^ $ | ( )
print("Metacharacter []")

# []
print("[] metacharacters")
lst = ["özcan", "özkan", "esra", "esin", "esma", "özhan", "özlem"]

search_key = "öz[chk]an"  # !!!!!
for i in lst:
    match = re.search(search_key, i)
    if match:
        print(match.group())
# özcan
# özkan
# özhan
print()

###
##
#
a = ["23BH56", "TY76Z", "4Y7UZ", "TYUDZ", "34534"]
# find startwith number
for i in a:
    if re.match("[0-9]", i):
        print(i)
# 23BH56
# 4Y7UZ
# 34534
print()

###
##
# find "TY76Z"

for i in a:
    if re.match("[A-Z][A-Z][0-9]", i):
        print(i)
print()
print("-" * 30)
###
##
# .(dot)
print("Metacharacter .(dot)")

# example 1
lst = ["özcan", "özkan", "esra", "esin", "esma", "özhan", "özlem"]
for i in lst:
    m = re.match("öz.an", i)
    if m:
        print(m.group())
# özcan
# özkan
# özhan

print()
print("-" * 30)
# example 2
a = ['23BH56', 'TY76Z', '4Y7UZ', 'TYUDZ', '34534', "1agAY54"]
for i in a:
    if re.match(".[0-9az]", i):
        print(i)
# 23BH56
# 34534
# 1agAY54

print()
print("-" * 30)

# example 3
lst = ["st", "sat", "saat", "saaat", "falanca"]
for i in lst:
    if re.match("sa*t", i):
        print(i)
# st
# sat
# saat
# saaat

print()
print("-" * 30)

# example 4
lst = ["ahmet", "kemal", "kamil", "mehmet"]
for i in lst:
    if re.match(".met", i):
        print(i)
# None
# good
lst = ["ahmet", "kemal", "kamil", "mehmet", "met", "kısmet", "ismet"]
for i in lst:
    if re.match(".*met", i):
        print(i)
# ahmet
# mehmet
# met
# kısmet
# ismet   :)))))))))

print()
print("-" * 30)
###
##
# + (plus) metacharacter
print("+ (plus) metacharacter")
lst = ["ahmet", "kemal", "kamil", "mehmet", "met", "kısmet", "ismet"]
for i in lst:
    if re.match(".+met", i):  # Not Found "met"
        print(i)
# ahmet
# mehmet
# kısmet
# ismet
print()
lst = ["st", "sat", "saat", "saaat", "falanca"]
for i in lst:
    if re.match("sa+t", i):
        print(i)
# sat
# saat
# saaat

print()
print("-" * 30)
###
##
# ? (question mark) metacharacter
print("? (question mark) metacharacter")

print(". (dot)")
lst = ["st", "sat", "saat", "saaat", "falanca"]
for i in lst:
    if re.match("sa.t", i):
        print(i)
# saat

print()
print("* (star)")
lst = ["st", "sat", "saat", "saaat", "falanca"]
for i in lst:
    if re.match("sa*t", i):
        print(i)
# st
# sat
# saat
# saaat


print()
print("+ (plus)")
lst = ["st", "sat", "saat", "saaat", "falanca"]
for i in lst:
    if re.match("sa+t", i):
        print(i)
# sat
# saat
# saaat


print()
print("? (question mark)")
lst = ["st", "sat", "saat", "saaat", "falanca"]
for i in lst:
    if re.match("sa?t", i):
        print(i)
# st
# sat

print()
# example
# find "uluslararası", "uluslar arası", "Uluslararası"
text = """Uluslararası hukuk, uluslar arası ilişkiler altında bir
disiplindir. Uluslararası ilişkilerin hukuksal boyutunu bilimsel bir
disiplin içinde inceler. Devletlerarası hukuk da denir. Ancak uluslar
arası ilişkilere yeni aktörlerin girişi bu dalı sadece devletlerarası
olmaktan çıkarmıştır."""

match = re.findall("[Uu]luslar ?arası", text)
for i in match:
    print(i)
# Uluslararası
# uluslar arası
# Uluslararası
print()
print("-" * 30)
###
##
# {} (Curly Braces) metacharacter
print("{} (Curly Braces) metacharacter")

lst = ["st", "sat", "saat", "saaat", "falanca"]
for i in lst:
    if re.match("sa{3}t", i):
        print(i)
# saaat
print()

for i in lst:
    if re.match("sa{1,3}t", i):
        print(i)
# sat
# saat
# saaat

print()
print("-" * 30)
###
##
# ^ (XOR) metacharacter
# find startwith and except
print("^ (XOR) metacharacter")

print()
# example 1
a = ['23BH56', 'TY76Z', '4Y7UZ', 'TYUDZ', '34534', "1agAY54"]
for i in a:
    if re.search("[A-Z]+[0-9]", i):
        print(i)
# 23BH56
# TY76Z
# 4Y7UZ
# 1agAY54

print()
# example 2
for i in a:
    m = re.search("[A-Z]+[0-9]", i)
    if m:
        print(m.group())
# BH5
# TY7
# Y7
# AY5

print()
for i in a:
    if re.match("[A-Z]+[0-9]", i):
        print(i)

# TY76Z
# or
print()
for i in a:
    nesne = re.search("^[A-Z]+[0-9]", i)
    if nesne:
        print(nesne.group())

# TY7
print()
a = ['23BH56', 'TY76Z', '4Y7UZ', 'TYUDZ', '34534', "1agAY54"]
# all except "1agAY54"
for i in a:
    m = re.match("[0-9A-Z][^a-z]+", i)
    if m:
        print(m.group())

print()
print("-" * 30)
###
##
# $ (Dollar) metacharacter
# find endwith
print("$ (Dollar) metacharacter")

print()
lst = ["at", "katkı", "fakat", "atkı", "rahat",
       "mat", "yat", "sat", "satılık", "katılım", "atveyat", "atat"]

# ending with ".....at"
for i in lst:
    if re.search("at$", i):
        print(i)
# at
# fakat
# rahat
# mat
# yat
# sat
# atveyat
print()

# starting with "at....."
for i in lst:
    if re.search("^at", i):
        print(i)
# at
# atkı
# atveyat
print()

# starting with and ending with "at.....at"
for i in lst:
    if re.search("^at$", i):
        print(i)
# at
# atkı


print()
print("-" * 30)
###
##
# \ (Back slash) metacharacter
print("\ (Back slash) metacharacter")

print()
lst = ["10$", "25€", "20$", "10TL", "25£"]
for i in lst:
    if re.match("[0-9]+$", i):
        print(i)
# None
for i in lst:
    if re.match("[0-9]+\$", i):
        print(i)
# 10$
# 20$


print()
print("-" * 30)
###
##
# | (Pipe) metacharacter
# or
print("| (Pipe)  metacharacter")

print()
lst = ["at", "katkı", "fakat", "atkı", "rahat",
       "mat", "yat", "sat", "satılık", "katılım", "atveyat", "atat"]
for i in lst:
    if re.search("^at|at$", i):
        print(i)
# at
# fakat
# atkı
# rahat
# mat
# yat
# sat
# atveyat
# atat


print()
print("-" * 30)
###
##
# () (parentheses) metacharacter
# groupping
print("() (parentheses)  metacharacter")

print()

import re
from urllib.request import urlopen

url = "https://web.archive.org/web/20121025012131/http://www.istihza.com/py2/icindekiler_python.html"
f = urlopen(url)

çıktı = "Başlık: {};\nBağlantı: {}\n"
regex = 'href="(.+html)">(.+)</a>'

for i in f:
    nesne = re.search(regex, str(i, 'utf-8'))
    if nesne:
        print(çıktı.format(nesne.group(2),
                           nesne.group(1)))
