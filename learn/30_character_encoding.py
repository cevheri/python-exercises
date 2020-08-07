# ASCII Table
# http://www.asciitable.com/
for i in range(128):
    if i % 4 == 0:
        print("\n")
    print("{:<3}{:>8}\t".format(i, repr(chr(i))), sep="", end="")
print()
# TR
print("ü".encode("cp857"))
# b'\x81'
print(int("81", 16))  # 129

# ISO-8859-1
# http://www.fileformat.info/info/charset/ISO-8859-1/list.htm


# UNICODE
# http://www.unicode.org/versions/Unicode6.2.0/UnicodeStandard-6.2.pdf
# a = u+ 0061
# 61 = int("61", 16) = 97= ASCII


# UTF-8
# http://www.fileformat.info/info/charset/UTF-8/list.htm

for i in range(1, 5):
    print("{} byte =>  2**{:<2} = {:,} bit ".format(i, i * 8, (2 ** (i * 8))))

# utf-8 tr language byte
characters = "abcçdefgğhıijklmnoöprsştuüvyz"
for s in characters:
    print("{:<5}{:<15}{:<15}".format(s,
                                     str(s.encode("utf-8")),
                                     len(s.encode("utf-8"))))
# 'ç'.encode('utf-8')
# b'\xc3\xa7

# int('c3a7', 16) # 50087
# bin(50087) # '0b1100001110100111'


unicodes = ['UTF-8', 'cp1254', 'latin-1', 'ASCII']
c = 'İ'
for u in unicodes:
    try:
        print("'{}' karakteri {} ile {} olarak "
              "ve {} sayısıyla temsil edilir.".format(c, u,
                                                      c.encode(u),
                                                      ord(c)))
    except UnicodeEncodeError:
        print("'{}' karakteri {} ile temsil edilemez!".format(c, u))

# "bu Türkçe bir cümledir.".encode("ascii", errors="strict")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# UnicodeEncodeError: 'ascii' codec can't encode character '\xfc' in
# position 4: ordinal not in range(12

print("bu Türkçe bir cümledir.".encode("ascii", errors="ignore"))
# b'bu Trke bir cmledir.'

print("bu Türkçe bir cümledir.".encode("ascii", errors="replace"))
# b'bu Trke bir cmledir.'

"bu Türkçe bir cümledir.".encode("ascii", errors="xmlcharrefreplace")
# b'bu T&#252;rk&#231;e bir c&#252;mledir.'


# encoding

import locale

print(locale.getpreferredencoding())  # utf-8

f = open("README.md", encoding="utf_8", errors='replace')  # UNICODE Replacement Character
print(f.read())

##########################
# repr()
print('\n')  #
print(repr('\n'))  # \n

# ascii()

print(repr("asd"))  # 'asd'
print(ascii("asd"))  # 'asd'

# but
print(repr("İ"))  # İ
print(ascii("İ"))  # \\u0130
# or
print(repr("€"))  # "'€'"
print(ascii("€"))  # "'\\u20ac'"
print("€".encode("unicode_escape"))  # b'\\u20ac'

# ord()
print(ord("\n"))  # 10
print(ord("€"))  # 8364

# chr()
print(chr(10)) # '\n'
print(chr(8364)) # '€'
