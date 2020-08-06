# Python Object Oriented programming
# Class Members
# -> instance -> Subclass -> Superclass -> object (built-in type)
# ref: https://stackoverflow.com/questions/12409714/python-class-members
#
# inheritance
# base class
# subclass
# super
# object class


class Cls:
    pass

class Cls():
    pass

class Cls(object):
    pass

# base class
class Printer():
    def __init__(self, name):
        self.name = name
        self.paper_size = []

    def do_print(self):
        print("{} Print".format(self.name))


# Subclass
class LazerPrinter(Printer):
    def __init__(self, name):
        super().__init__(name)
        self.paper_size = ["A4", "A5"]

    # move to super class
    # def __init__(self):
    #     self.name = "Printer"
    #
    # def do_print(self):
    #     print("Printer Print")


# Subclass
class Fax(Printer):
    def __init__(self, name):
        super().__init__(name)
        self.paper_size = ["A3", "A4", "A5"]

    # move to super class
    # def __init__(self):
    #     self.name = "Fax"
    #
    # def do_print(self):
    #     print("Fax Print")
    fax_number = 0

    def do_fax(self):
        print("Send Fax")


# SUBCLASS
class A4Printer(Printer):
    def __init__(self, name):
        super().__init__(name)
        self.paper_size = ["A4"]


lp = LazerPrinter("Lazer")
print(lp.do_print())
# print(lp.do_fax())

fp = Fax("Fax")
print(fp.do_print())
print(fp.do_fax())
fp.fax_number = 1
print(fp.fax_number)
