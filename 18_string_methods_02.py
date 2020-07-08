#  String methods
#
#    capitalize()
#    title()
#    swapcase()
#    casefold()
#    strip(), lstrip(), rstrip()
#    join()
#    count()
#    index(), rindex()
#    find, rfind()
#    center()
#    rjust(), ljust()
#    zfill()
#    partition(), rpartition()
#    encode()
#    expandtabs()

#    capitalize()
print()
print("capitalize()", "-" * 30, sep="\n")
a = "python"
print(a)
print(a.capitalize())

b = "python programming language"
print(b.capitalize())
print()
#    title()
print("title()", "-" * 30, sep="\n")
print(b.title())
print()
# swapcase()
print("swapcase()", "-" * 30, sep="\n")
c = "Python Programming LANGUAGE"
print(c.swapcase())
print()
# casefold()
print("casefold()", "-" * 30, sep="\n")
print("ÜĞİŞÇÖ".lower())
print("ÜĞİŞÇÖ".casefold())
print("ß".lower())  # ß
print("ß".casefold())  # ss
print()
# strip(), lstrip(), rstrip()
print("strip()", "-" * 30, sep="\n")
c = " pyt hon "
print(c.strip())  # ' ', '\t', '\n', '\r', '\v', '\f'
print()

print("mom".strip("m"))  # o
print("mom".rstrip("m"))  # om
print("mom".lstrip("m"))  # mo
print()
# join()
print("join()", "-" * 30, sep="\n")
c = "Python Programming Language"
d = c.split()
print(d)  # ['Python', 'Programming', 'Languga']
print(" ".join(d))  # Python Programming Language
print()

# count()
print("count()", "-" * 30, sep="\n")
c = "Python Programming Language"
print(c.count("P", 1, 100))
print()

# index(), rindex()
print("index()", "-" * 30, sep="\n")
c = "Python Programming Language"
print(c.index("P", 1, 100))
print()
#
# for r in range(len(c)):
#     print(c.index("P", r))
# if r == c.index("P", r):
#     print(r)

print("rindex()", "-" * 30, sep="\n")
print(c.rindex("P"))
print()

# find, rfind() like  index(), rindex(), notfound = -1
print("count()", "-" * 30, sep="\n")
c = "Python Programming Language"

for r in range(len(c)):
    if r == c.find("P", r):
        print(r)

print()

# center()
print("center()", "-" * 30, sep="\n")
c = "Python Programming Language"
print(c.center(100))
print()

for r in range(1, 20):
    print("python".center(r,"-"))

print()

# rjust(), ljust()
print("rjust(), ljust()", "-" * 30, sep="\n")
c = "python"
print(c.rjust(10, "."))
print(c.ljust(10,"."))
print()

print()

# zfill()
print("zfill()", "-" * 30, sep="\n")
for r in (range(11)):
    print(str(r).zfill(2))


print()

# partition(), rpartition()
print("partition(), rpartition()", "-" * 30, sep="\n")

c = "Python Programming Language"
d = "Python"
print(a.partition("t"))
print(d.partition(" "))


print("qazÜĞİŞÇÖIıiqaz".encode("cp1254"))

print("Python   Programming\tLanguage".expandtabs(100))