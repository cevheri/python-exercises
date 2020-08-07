# python Object Oriented Programming
#
# class methods
# instance methods

class EmployeeClass01():
    persons = []

    # instance method
    def __init__(self, name):
        self.name = name
        self.add()

    # instance method
    def add(self):
        self.persons.append(self.name)

    # instance method
    def delete(self):
        self.persons.append(self.name)

    # class method
    # !!!!!!! wrong
    def view(self):
        print(len(self.persons))


# EmployeeClass01.view();

e01 = EmployeeClass01("Python")
e01.view()  # 1

e01_1 = EmployeeClass01("Java")
e01_1.view()  # 2

##############
print()
# @classmethod decorator
print("@classmethod decorator")


class EmployeeClass02():
    persons = []

    # instance method
    def __init__(self, name):
        self.name = name
        self.add()

    # instance method
    def add(self):
        self.persons.append(self.name)

    # instance method
    def delete(self):
        self.persons.append(self.name)

    # class method
    # good
    @classmethod
    def view(cls):
        print(len(cls.persons))


# good
EmployeeClass02.view()  # 0
##
emp_02 = EmployeeClass02("csharp")
# bad
emp_02.view()  # 1
##
emp_02_1 = EmployeeClass02("go")
# bad
emp_02_1.view()  # 2

#####################################
#
# alternative constructor
print("alternative constructor")

book_list = [('9789753424080', 'Greenberg', 'Sana Gül Bahçesi Vadetmedim', 'Metis'),
             ('975872519X', 'Evren', 'Postmodern Bir Kız Sevdim', 'İthaki'),
             ('9789754060409', 'Nietzsche', 'Böyle Buyurdu Zerdüşt', 'Cem')]


###################################
# bad
def query(key=None, val=None):
    for li in book_list:
        if not key and not val:
            print(*li, sep=', ')

        elif key == 'isbn':
            if val == li[0]:
                print(*li, sep=', ')

        elif key == 'author':
            if val == li[1]:
                print(*li, sep=', ')

        elif key == 'name':
            if val == li[2]:
                print(*li, sep=', ')

        elif key == 'publisher':
            if val == li[3]:
                print(*li, sep=', ')


query("isbn", "9789753424080")
query("author", "Greenberg")
# query()
print()


###################################
# bad
def query2(key=None, val=None):
    d = {"isbn": [li for li in book_list if val == li[0]],
         "author": [li for li in book_list if val == li[1]],
         "name": [li for li in book_list if val == li[2]],
         "publisher": [li for li in book_list if val == li[3]]}
    for element in d.get(key, book_list):
        print(*element, sep=", ")


query2("isbn", "9789753424080")

print()


#####################################
# bad
def find(val, index):
    return [li for li in book_list if val == li[index]]


def query2(key=None, val=None):
    d = {"isbn": find(val, 0),
         "author": find(val, 1),
         "name": find(val, 2),
         "publisher": find(val, 3)}
    for element in d.get(key, book_list):
        print(*element, sep=", ")


query2("author", "Greenberg")
# query2()
print()


#############################################
# class level
class Query():
    def __init__(self, val=None, index=None):
        self.books = [('9789753424080', 'Greenberg', 'Sana Gül Bahçesi Vadetmedim', 'Metis'),
                      ('975872519X', 'Evren', 'Postmodern Bir Kız Sevdim', 'İthaki'),
                      ('9789754060409', 'Nietzsche', 'Böyle Buyurdu Zerdüşt', 'Cem')]
        if not val and not index:
            l = self.books
        else:
            l = [li for li in self.books if val == li[index]]
        for i in l:
            print(*i, sep=", ")

    @classmethod
    def by_isbn(cls, isbn):
        cls(isbn, 0)

    @classmethod
    def by_author(cls, author):
        cls(author, 1)

    @classmethod
    def by_name(cls, name):
        cls(name, 2)

    @classmethod
    def by_publisher(cls, publisher):
        cls(publisher, 3)


all_books = Query()
# Query.by_isbn()
Query.by_author("Greenberg")
# Query.by_name()
# Query.by_publisher()

##################################################
# decorator example class
# data class

"""class date:
    __slots__ = '_year', '_month', '_day'

    def __new__(cls, year, month=None, day=None):
        if (isinstance(year, bytes) and len(year) == 4 and
            1 <= year[2] <= 12 and month is None):  # Month is sane
            # Pickle support
            self = object.__new__(cls)
            self.__setstate(year)
            return self
        _check_date_fields(year, month, day)
        self = object.__new__(cls)
        self._year = year
        self._month = month
        self._day = day
        return self

    @classmethod
    def fromtimestamp(cls, t):
        y, m, d, hh, mm, ss, weekday, jday, dst = _time.localtime(t)
        return cls(y, m, d)

    @classmethod
    def today(cls):
        t = _time.time()
        return cls.fromtimestamp(t)

    @classmethod
    def fromordinal(cls, n):
        y, m, d = _ord2ymd(n)
        return cls(y, m, d)
        
decorator function
datetime.date(2020,10,10)
datetime.date.today()

"""
print("-" * 60)
print()

#########################################
#
# static method

# bad way
print("Instance Method")


class CustomMathInstance():
    def pi(self):
        return 22 / 7

    def square_root(self, number):
        return number ** 0.5


# CustomMathInstance.pi() error
m = CustomMathInstance()
print(m.pi())

print()
##############################
# bad way
print("Class Method")


class CustomMathClass():
    @classmethod
    def pi(cls):
        return 22 / 7

    @classmethod
    def square_root(cls, number):
        return number ** 0.5


print(CustomMathClass.pi())

print()
#####################################
# good
print("Static Method")


class CustomMathStatic():
    @staticmethod
    def pi():
        return 22 / 7

    @staticmethod
    def square_root(number):
        return number ** 0.5


print(CustomMathStatic.pi())
print(CustomMathStatic.square_root(4))
