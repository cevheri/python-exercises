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


emp_1 = Employee('John', 'Smith')
print(emp_1.email)
print(emp_1.last)
print(emp_1.email)
print(emp_1.fullname)
