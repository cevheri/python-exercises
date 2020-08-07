# Python Programming Language
# construction
# initialization
# destruction
#
# __new__() method
print("OOP __new__() Method")
print()


class CustomClass:
    def __new__(cls, *args, **kwargs):
        print("new method")
        return super().__new__(cls, *args, **kwargs)
        #return object.__new__(cls, *args, **kwargs)

    def __init__(self):
        print("init method")


c = CustomClass()
# new method
# init method