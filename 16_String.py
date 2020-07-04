# String

val = "Python"
numbers = "0123456789"

for p in val:
    print(p)

print("1#" * 30)
##############################
print(*val, sep="\n")

print("2#" * 30)
##############################
for n in numbers:
    print(int(n) * 2)

print("3#" * 30)
##############################
print(val[0])  # P -> first
print(val[-1])  # n -> last

for i in range(6):
    print(val[i])

for i in range(len(val)):
    print(val[i])

print("4#" * 30)
##############################
val2 = "www.python.org"
print(val2[0:3])  # www
print(val2[:3])  # www
print(val2[4:10])  # python
print(val2[11:14])  # org

print("5#" * 30)
##############################
s1 = "www.google.com"
s2 = "www.amazon.com"
s3 = "www.twitter.com"
s4 = "www.linux.com"

for s in s1, s2, s3, s4:
    print("web site : ", s[4:-4])
# web site :  google
# web site :  amazon
# web site :  twitter
# web site :  linux
print("6#" * 30)
##############################
# "www.python.org"
print(val2[::-1])  # gro.nohtyp.www
print(val2[9:3:-1])  # nohtyp

print(val2[::2])  # wwpto.r
print(val2[::-2])  # gonhy.w
print("7#" * 30)
##############################
# reversed
print(*reversed(val2))  # g r o . n o h t y p . w w w
print("8#" * 30)
##############################
# sorted
print(*sorted(val2))  # . . g h n o o p r t w w w y

print("7#" * 30)
##############################
# for turkish locale
val_tr = "CEVHERİ"
import locale

# locale.setlocale(locale.LC_ALL, 'Turkish_Turkey.1254')  # for windows
# locale.setlocale(locale.LC_ALL, 'tr_TR')  # linux
#print(*sorted(val_tr, key=locale.strxfrm), sep="")

# good
characters = "abcçdefgğhıijklmnoöprsştuüvyz"
tr_sort = {i: characters.index(i) for i in characters}
# print(*sorted(val_tr, key=tr_sort), sep="")

print("8#" * 30)
##############################
print(*dir(str))
print("-"*30)
count=0
for i in dir(str):
    if "_" not in i[0]:
       count +=1
       print(count,i)
print("-"*30)
print(*enumerate(val_tr),sep="\n")
print("-"*30)
for row, method in enumerate(dir(str)):
    print(row, method)
print("9#" * 30)
##############################


print("7#" * 30)
##############################
