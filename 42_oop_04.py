# Python Object Oriented programming
# Class Members
# -> instance -> Subclass -> Superclass -> object (built-in type)
# ref: https://stackoverflow.com/questions/12409714/python-class-members
#
# public variables
# private variables
# semi-private variables

class First:
    pass


f = First()


class CustomClass():
    __private = "Private Class Variable"  # private Variable
    __private_ = ""  # private Variable
    __private_element = ""  # private Variable
    __private_element_ = ""  # private Variable

    _semi_private = "Semi Private Variable"  # Semi Private Variable

    class_attribute = "class_attribute"  # public
    print("Class Attribute")

    def __init__(self):  # public
        self.instance_attribute = "instance_attribute"
        print("init method")

    def instance_method(self):  # public
        print("instance method")
        print(self.__private)  # !!! access

    @classmethod
    def class_method(cls):  # public
        print("Class Method")

    @staticmethod
    def static_method():  # public
        print("Static Method")


c = CustomClass()

# c.__private_element > access error
# CustomClass.__private > access error


# name mangling
# !!!!! (_ + Class Name+ private variable name)
print(c._CustomClass__private)
print()
print("-" * 30)


###############################################
#
# @property

class Person():
    _people = []

    def __init__(self, name):
        self._name = name
        self.add_person()

    def add_person(self):
        self._people.append(self._name)
        print("{} has been added to the list".format(self._name))

    @classmethod
    def view_person(cls):
        print("Person List")
        for person in cls._people:
            print(person)

    # !!!
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        person = self._people.index(self._name)
        self._people[person] = new_name
        print("Name Updated, new name:", new_name)


person = Person("Guido van")
print(person.view_person())  # Guido

person.name = "Rossum"
print(person.view_person())  # Rossum

print()
print("-" * 30)


###
#
# method to variable
class Program():
    def __init__(self):
        self._version = "0.0.0"
        self._minor_version = "0"

    def version_info(self):  # method
        return "v"+self._version

    @property
    def version(self):  # read only variable
        return self._version

    @property
    def minor_version(self):
        return self._minor_version

    @minor_version.setter # check and set variable
    def minor_version(self, new_value):
        if new_value =="v":
            print("Error")
        else:
            self._minor_version = new_value
        return self._minor_version

    @minor_version.deleter
    def minor_version(self):
        del self._minor_version


program = Program()
program.version_info()  # method
program.version  # variable

# and read only version
# program.version = "1.0.0"  # AttributeError: can't set attribute
# and
program.minor_version  ="1"
