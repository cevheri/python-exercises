# String Methods format {}


name = "Cevheri"
print('-' * 30)
############################################
# format
print("Name is %s." % name)
print("Name is {}.".format(name))
print("Name is {:s}.".format(name))  # bad
print("Name is", name + ".")
print('-' * 30)
############################################
print("First name {0}, last name {0}".format(name))
print('-' * 30)
############################################
print("|{:>20}|".format(name))
print("|{:<20}|".format(name))
print("|{:^20}|".format(name))

print('-' * 30)
############################################
# example
for row, c in enumerate(dir(str)):
    if row % 3 == 0:
        pass
#        print("\n", end="|")
# old    print("%-20s|" %c, end="")
# new   print("{:<20}|".format(c), end="")
print()
print('-' * 30)
############################################
# {:c} 0..256
# print("{:c}".format("a"))
print("{:c}".format(97))  # a
print('-' * 30)
############################################
# {:d}
print("{:d}".format(97))  # 97
print('-' * 30)
############################################
# {:o} octal
print("{:o}".format(65))  # 101
print('-' * 30)
############################################
# {:x} hexadecimal
print("{:x}".format(65))  # 41
print('-' * 30)
############################################
# {:b}
print("{:b}".format(2))  # 10
print('-' * 30)
############################################
# {:f} float
print("{:.2f}".format(65))  # 65.00
print('-' * 30)
############################################
# {:,}
print("{:,}".format(123456789))  # 123,456,789
print('-' * 30)
############################################
