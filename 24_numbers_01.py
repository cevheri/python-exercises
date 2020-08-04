# number systems

# ref: https://docs.python.org/3/library/functions.html

# 10
number_systems = ["10"]
print(("{:^5} "*len(number_systems)).format(*number_systems))
for i in range(17):
    print("{0:^5}".format(i))
print('-' * 30)
# convert 1980 :
# (0 * (10 ** 0)) + (8 * (10 ** 1)) + (9 * (10 ** 2)) + (1 * (10 ** 3))
###################################################################
# 8
number_systems = ["10", "8"]
print(("{:^5} "*len(number_systems)).format(*number_systems))
for i in range(17):
    print("{0:^5} {0:^5o}".format(i))
print('-' * 30)
# 3674 > 1980 :
# (4 * (8 ** 0)) + (7 * (8 ** 1)) + (6 * (8 ** 2)) + (3 * (8 ** 3))
###################################################################

# 16

number_systems = ["10", "8","16"]
print(("{:^5} "*len(number_systems)).format(*number_systems))
for i in range(17):
    print("{0:^5} {0:^5o} {0:^5x}".format(i))
print('-' * 30)
# convert 7bc -> 10
#     a –> 10
#
#     b –> 11
#
#     c –> 12
#
#     d –> 13
#
#     e –> 14
#
#     f –> 15
# 7bc >>> 1980 :
# ((12 * (16 ** 0)) + ((11 * (16 ** 1)) + ((7 * (16 ** 2))
###################################################################
number_systems = ["10", "8","16","2"]
print(("{:^5} "*len(number_systems)).format(*number_systems))
for i in range(17):
    print("{0:^5} {0:^5o} {0:^5x} {0:^5b}".format(i))
print('-' * 30)

# 1100 > 12
# (0 * (2 ** 0)) + (0 * (2 ** 1)) + (1 * (2 ** 2)) + (1 * (2 ** 3))


bin(2)

'0b10'
bin(2)[2:]

'10'

hex()

# Bu fonksiyon, herhangi bir sayıyı alıp, o sayının on altılı sistemdeki karşılığını verir:

# >>> hex(10)

'Oxa'
oct()

# Bu fonksiyon, herhangi bir sayıyı alıp, o sayının sekizli sistemdeki karşılığını verir:

# oct(10)

'0o12'

int('7bc', 16)

1980

#>>> int('1100', 2)

12

#>>> int('1100', 16)

4352


for i in range(256):
    print(i, bin(i)[2:], hex(i)[2:])










