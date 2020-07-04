# Exception Handling
# try except

try:
    a = int(input("value1 :"))
    b = int(input("value2 : "))
    print(a+b)
except ValueError:
    print("Please Number")
