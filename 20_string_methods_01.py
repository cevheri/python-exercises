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
for r in range(10):
    print("|%15s|" % r)

print("|%s|" % name.rjust(15))
print("|%s|" % name.ljust(15))  # or %rjust(-15

print('-' * 30)
############################################

print("First name %(first_name)s, last name %(last_name)s"
      % {"first_name": name, "last_name": name})

print('-' * 30)
############################################


print('-' * 30)
############################################


print('-' * 30)
############################################


print('-' * 30)
############################################
