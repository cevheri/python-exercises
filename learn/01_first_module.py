import sys


print(sys.executable)
print(sys.version)


class Employee:
    """A Simple Employee class"""

    def __init__(self, first, last):
        """ init method açıklaması"""
        self.first = first
        self.last = last

    @property
    def email(self):
        """ email method açıklaması"""
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        """ full name method açıklaması"""
        return '{} {}'.format(self.first, self.last)


print("\n")
emp_1 = Employee('John', 'Smith')
print("First Name:", emp_1.first)
print("Last Name:", emp_1.last)
print("Email: ", emp_1.email)
print("Full Name:", emp_1.fullname)
