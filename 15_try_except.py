# Exception Handling
# try except
# basic try

try:
    a = int(input("Value 1 : "))
    b = int(input("Value 2 : "))
    print(a + b)
except ValueError:
    print("Please Number")
##################################
# except 2 error
try:
    a = int(input("Value 1 : "))
    b = int(input("Value 2 : "))
    print(a / b)
except ValueError:
    print("Please Number")
except ZeroDivisionError:
    print("Division By Zero")
##################################
# except 2 error -> custom
try:
    a = int(input("Value 1 : "))
    b = int(input("Value 2 : "))
except ValueError:
    print("Please Number")
else:
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Division By Zero")
##################################
# except 2 error -> custom 2
try:
    a = int(input("Value 1 : "))
    b = int(input("Value 2 : "))
    print(a / b)
except (ValueError, ZeroDivisionError):
    print("Handled Exception")
##################################
# try as -> error message
try:
    a = int(input("Value 1 : "))
    b = int(input("Value 2 : "))
    print(a + b)
except ValueError as err:
    print("Please Number. Exception Message : ", err)
##################################
# try except finally
try:
    f = open("NoneFile.txt")
except IOError:
    print("File read/write Error")
finally:
    f.close()
##################################
# raise error
try:
    a = int(input("Value 1 : "))
    b = int(input("Value 2 : "))
    if b == 0:
        raise ZeroDivisionError("Division By Zero")
    print(a / b)
except ValueError:
    print("Please Number")
##################################
# assert error
try:
    a = int(input("Value 1 : "))
    b = int(input("Value 2 : "))
    assert b == 0, "Division By Zero"
    print(a / b)
except ValueError:
    print("Please Number")

##################################
# handled all exception
try:
    a = int(input("Value 1 : "))
    b = int(input("Value 2 : "))
    print(a / b)
except Exception as ex:
    print("Handled Exception", ex)
#################################
# handled all exception 2
try:
    a = int(input("Value 1 : "))
    b = int(input("Value 2 : "))
    print(a / b)
except:
    print("Handled Exception")
################################
