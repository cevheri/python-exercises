# for loops

name = "Cevheri"

print(*name, sep="\n")
print(*"-" * 30)
key = 0
while key < len(name):
    print("While loop : ", name[key])
    key += 1
print(*"-" * 30)
for a in name:
    print("For Loop: ", a)

print(*range(10), sep="\n")

for i in range(0, 10):  # range(10)
    print("Range Value real: ", i)

for i in range(1, 10, 2):  # range(10)
    print("Range Value Even Number: ", i)

for i in range(10, 0, -1):
    print("Range Value Minus Number: ", i)

print(*"-" * 30)

for i in range(5):
    print(i)
    # if i > 5:
    if i == 4:
        break
else:
    print("printed else")
print(*"-" * 30)
############################
# example
a = "12345asdasfddgdhfjfdgdşfkgjdfklgşjdfklgjdfkghdfjghjklsdhajlsdhjkjhkhjjh6789"
b = "1234sdfsuıdoryeuıfsjkdfhdjklghjdfklruseldhfjlkdshfljskeeuf678"
c = ""
for s in a:
    if not s in b:
        c += s
else:
    print(c)

print(*"-" * 30)
#####################################################################################
# file compare example
f1 = open("output/names01", encoding="utf-8")
f1_line = f1.readlines()
f1.close()

f2 = open("output/names02", encoding="cp1254")
f2_line = f2.readlines()
f2.close()

for i in f2_line:
    if i in f1_line:
        print(i)

print(*"-" * 30)
#####################################################################################
text = "Cevheri Bozoglan"
key = "z"  # input("value")
val = 0
for s in text:
    if key == s:
        val += 1
print("counts:", val)

print(*"-" * 30)

#####################################################################################
key = "z"
val = 0
places_file = open("output/places")
for place_line in places_file:
    for place_key in place_line:
        if key == place_key:
            val += 1
print("key counts: ", val)
places_file.close()
