# String Methods
# str.replace()
import sys

val = "Python Programming Practice"
print(val.replace("P", "$"))
print(val)
# val = val.replace("P", "$") string change
print('-' * 30)

print(val.replace("P", "$", 2))
print(val.replace("P", "$", -1))
############################################
# split(), rsplit(), splitlines()

val = "Python, Programming, Practice"
print(val.split(" "))  # ['Python,', 'Programming,', 'Practice']
print(val.split(","))  # ['Python', ' Programming', ' Practice']
print(val.split(", ", 1))  # ['Python', 'Programming, Practice']

# python version check
print(sys.version.split())
# ['3.7.6', '(default,', 'Jan', '8', '2020,', '20:23:39)', '[MSC', 'v.1916', '64', 'bit', '(AMD64)]']

# rsplit()
print(val.rsplit(", ", 1))  # ['Python, Programming', 'Practice']

# splitlines()
line = """Python version vb..
Programming
Language"""
print(line.splitlines())  # ['Python version vb..', 'Programming', 'Language']
#######################################################################
# lower()
print(val.lower())

a = "İSTANBUL"
b = "ISTANBUL ÇAĞRI MÜŞÇÖı,"
print(a.lower())
print(b.lower())
print("istanbul")

# upper
print("istanbul".upper())

print("ISTANBUL".isupper())  # True
print("istanbul".islower())  # True
##############################
# endswith
print("istanbul".endswith("l"))  # True

print("istanbul".endswith("ul"))

# startswith
print("istanbul".startswith("is"))

