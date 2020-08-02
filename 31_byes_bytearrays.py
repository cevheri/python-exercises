# bytes


byte = b''
type(byte) # <class 'bytes'

###########################################
# b'ş'
#  File "<stdin>", line 1
# SyntaxError: bytes can only contain ASCII literal characters.

b = bytes("ş", "utf-8", errors="replace")
print(b) # b'\xc5\x9f'

###########################################
print(dir(bytes))
for i in dir(bytes):
     if i not in dir(str):
         print(i)
# decode
# fromhex
# hex

###########################################
# decode()

"İ".encode("utf-8") # b'\xc4\xb0'
"İ".encode("cp1254") # b'\xdd'
# not "İ".encode("ascii")

b"\xc4\xb0".decode("utf-8") # İ
b"\xc4\xb0".decode("cp1254") # 'Ä°' :)))
# not b"\xc4\xb0".decode("ascii")
###########################################
# fromhex()

bytes.fromhex("c4b0") # b'\xc4\xb0'

###########################################
# bytearrays

pdf = bytearray(b'PDF-1.7')
print(type(pdf))
# method list
"""
append
clear
copy
count
extend
index
insert
pop
remove
reverse
"""
"""
capitalize
center
count
decode
endswith
expandtabs
find
fromhex
index
isalnum
isalpha
isdigit
islower
isspace
istitle
isupper
join
ljust
lower
lstrip
maketrans
partition
replace
rfind
rindex
rjust
rpartition
rsplit
rstrip
split
splitlines
startswith
strip
swapcase
title
translate
upper
zfill
"""

































