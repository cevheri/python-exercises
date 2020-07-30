# String Methods format, %


name = "Cevheri"
if len(name) > 5:
    print(name[:5], "...", sep="")
else:
    print(name)

print('-' * 30)
############################################
# %
print("Name is %s" % name)

print('-' * 30)
############################################
print("First name %s, last name %s" % (name, name))
print('-' * 30)
############################################
for row, character in enumerate(name, 1):
    print("%s.character:'%s'" % (row, character))

print('-' * 30)
############################################
for r in range(10):
    print("%s" % r)

for r in range(10):
    print("%%%s" % r)

print('-' * 30)
############################################
# rjust, ljust
for r in range(10):
    print("|%15s|" % r)

print("|%s|" % name.rjust(15))
print("|%s|" % name.ljust(15))  # or %rjust(-15

print('-' * 30)
############################################
# variable
print("First name %(first_name)s, last name %(last_name)s"
      % {"first_name": name, "last_name": name})

print('-' * 30)
############################################
# %d %i
age = 35
print("I'm %s years old" % age)
print("I'm %d years old" % age)

print("%05d" % 30)  # 00023
print("%.5d" % 23)  # 00023
print("%10.5d" % 23)  # 00023
print("%010.d" % 23)  # 0000000023
"23".zfill(10)  # '0000000023'
print('-' * 30)
############################################
# %o octal
print("%i %o" % (10, 10)) # 10 12
print('-' * 30)
############################################
# %x hexadecimal
print("%i %x" % (20, 20)) # 20 14

print('-' * 30)
############################################
# %f float
print("%f" %1.2) # 1.200000 !!!!!!
print("%.1f" %1.2) # 1.2 :)
print('-' * 30)
############################################
# %c char
print("%c" %"A") # A
print("%c" %65) # A
for i in range(128):
    print("%s ==> %c" %(i, i))
print('-' * 30)
############################################
# example
for row, c in enumerate(dir(str)):
    if row%3==0:
        print("\n", end="|")
    print("%-20s|" %c, end="")
print()
print('-' * 30)
############################################
