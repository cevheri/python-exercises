# file methods

# open()
# create file
# delete and new file
open("26_first_text.txt", "w")

f = open("26_first_text.txt", "w")
f.close()

# write() file
f = open("26_first_text.txt", "w")
val = """First Line
Second Line
Third Line
"""
f.write(val)
f.close()

# read(), readline(), readlines()
f = open("26_first_text.txt")  # or f = open("26_first_text.txt", "r")
print(f.read())
# First Line
# Second Line
# Third Line
f.close()

f = open("26_first_text.txt")  # or f = open("26_first_text.txt", "r")
print(f.readline())  # First Line
print(f.readline())  # Second Line
print(f.readline())  # Third Line
print(f.readline())  # null
f.close()

####################################
# file closed
try:
    f = open("26_first_text.txt")  # or f = open("26_first_text.txt", "r")
    print(f.readlines())  # ['First Line\n', 'Second Line\n', 'Third Line\n']
except IOError:
    print("Error")
finally:
    f.close()

# file closed
with open("26_first_text.txt") as f:
    print(f.read())

# re-read
with open("26_first_text.txt") as f:
    print(f.read())
    f.seek(0)
    print(f.read())
    print(f.tell())

# file add()
with open("26_first_text2.txt", "a") as a:
    a.write("First Line\n")

with open("26_first_text.txt", "r+") as a:
    data = a.read()
    a.seek(0)
    a.write("Start Line\n" + data)


with open("26_first_text.txt", "r+") as f:
    data = f.readlines()
    data.insert(2, "Start Line (readlines and writelines)\n")
    f.seek(0)
    f.writelines(data)