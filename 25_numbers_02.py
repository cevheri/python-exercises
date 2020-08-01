# number systems

# int = 12
print([i for i in dir(int) if not i.startswith("_")])

# ['bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator','real', 'to_bytes']

# bit_length() or len(bin(10)[2:]

for i in range(11):
    print(i, bin(i)[2:], len(bin(i)[2:]), sep="\t")

val = 255
print(val.bit_length()) # or (10).bit_length()

print(len(bin(10)[2:]) == (10).bit_length()) # True

###################################################

# float = 12.5

print([i for i in dir(float) if not i.startswith("_")])

# ['as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']

# as_integer_ratio()
num = 4.5
print(num.as_integer_ratio()) # (9, 2)
# 9:2 = 4.5

# is_integer()

print((12.0).is_integer())
# True

print((12.5).is_integer())
# False
##########################################################

# complex  = 12+4j
print([i for i in dir(complex) if not i.startswith("_")])
# ['conjugate', 'imag', 'real']

print((12+4j).imag) # 4.0
print((12+4j).real) # 12.0

#########################################################
# Arithmetic Function

# complex()
# float()
# int()
# pow()
# round()
# hex()
# oct()
# bin()
# >>>>>>

# abs()
print(abs(-2)) # 2
print(abs(2)) # 2

# divmod()
print(divmod(10, 2)) # (5, 0)
# 10:2 = 5

print(divmod(14, 3)) # (4, 2)
# 14 // 3, 14 % 3

# max()
values = [882277, 403538, 441349, 721048, 32859]
print(max(values)) # 882277

names = ["Python", "Programming", "Language"]
print(max(names))







