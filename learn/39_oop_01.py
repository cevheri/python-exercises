# classes

class EmployeeClass01:
    firs_name = ""
    last_name = ""
    age = 0
    langs = []
    print("Running Employee Class 01")


EmployeeClass01  # print : # Running Employee Class 01
EmployeeClass01()  # not running print
print("create instance")

person1 = EmployeeClass01()  # not running print
person1.firs_name = "Cevheri"
person1.last_name = "Python"
person1.langs.append("tr")
person1.langs.append("en")
print(person1.langs)  # ['tr', 'en']

person2 = EmployeeClass01()  # not running print
print(person2.langs)  # ['tr', 'en'] :((
print()
########################################3
#
# __init__
print("__init__")


class EmployeeClass02():
    def __init__(self):
        self.langs = []
        print("Running Employee Class 02")


EmployeeClass02  # not running print
EmployeeClass02()  # Running Employee Class 02
e1 = EmployeeClass02()  # Running Employee Class 02
e2 = EmployeeClass02()  # Running Employee Class 02
print()
#####################
# class attribute and instance attribute
print("class attribute and instance attribute")


class EmployeeClass03():
    val = "Class Attribute"

    def __init__(self):
        self.val = "Instance Attribute"


e3 = EmployeeClass03()
print(e3.val)  # Instance Attribute

print(EmployeeClass03.val)  # Class Attribute

print()


#############################################
#
#
class EmployeeClass04():
    def __init__(self):
        self.langs = []


e4 = EmployeeClass04()
e4.langs.append("tr")
print(e4.langs)  # ['tr']
##
print()
e4_1 = EmployeeClass04()
e4_1.langs.append("en")
e4_1.langs.append("fr")
e4_1.langs.append("de")
print(e4_1.langs)  # ['en', 'fr', 'de']
# good example :)
print()


########################
#
#
class EmployeeClass05():
    persons = []

    def __init__(self, name):
        self.name = name
        self.add()

    def add(self):
        self.persons.append(self.name)

    def delete(self):
        EmployeeClass05.persons.append(self.name)


e5 = EmployeeClass05("Cevheri")
print(e5.name)  # Cevheri
print(e5.persons)  # ['Cevheri']

e5_02 = EmployeeClass05("Python")
print(e5_02.name)  # Python
print(e5_02.persons)  # ['Cevheri', 'Python']
