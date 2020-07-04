"""
+	Add two operands or unary plus	                                    x + y+ 2
-	Subtract right operand from the left or unary minus	                x - y- 2
*	Multiply two operands	                                            x * y
/	Divide left operand by the right one (always results into float)	x / y
%	Modulus - remainder of the division of left operand by the right	x % y (remainder of x/y)
**	Exponent - left operand raised to the power of right	            x**y (x to the power y)
//	Floor division - division that results into whole number adjusted to the left in the number line	x // y
"""
print(2 + 1)
print(2 - 1)
print(2 * 1)
print(2 / 1)
print(2 % 1)
print(2 ** 1)
print(2 // 1)
###################################
"""
bool(x) -> bool
Returns True when the argument x is true, False otherwise.
The builtins True and False are the only two instances of the class bool.
The class bool is a subclass of the class int, and cannot be subclassed.
"""
bool(3)  # True
bool("tree")  # True
bool(" ")  # True
bool("0")  # True
bool(0)  # False  !!!!!!
bool("")  # False

###################################
# and or not
# x = int(input("Your Note:"))
x = 100
if not x:
    print("Not Value")
elif x > 100 or x < 0:
    print("No such note")
elif x >= 90 and x <= 100:  # :)) 90 <= x <= 100:
    print("You got A.")
elif x >= 80 and x <= 89:
    print("You got B.")
elif x >= 70 and x <= 79:
    print("You got a C.")
elif x >= 60 and x <= 69:
    print("You got D.")
elif x >= 0 and x <= 59:
    print("You got an F.")

###################################
# =, +=, -=
p = 10

# difficult
p = p + 2

# easy
p += 2
print(p)
###########
# difficult
p = p - 2

# easy
p -= 2
print(p)
###########

# difficult
p = p / 2

# easy
p /= 2
print(p)
###########
# difficult
p = p * 2

# easy
p *= 2
print(p)
###########
# difficult
p = p % 2

# easy
p %= 2
print(p)
###########
# difficult
p = p ** 2

# easy
p **= 2
print(p)
###########
# difficult
p = p // 2

# easy
p //= 2
print(p)
######################################################
# :=  python >=3.8 version
# if (entry := len(input("What is your name?"))) < 4:
#     print("Your name was short.")
# elif entry < 6:
#     print("Your name is a little long.")
# else:
#     print("You have a very long name.")
######################################################
# in keyword
name = "Cevheri Bozoğlan"
print("e" in name)
######################################################
# id() function
p = 10
y = 10
t = 11
print(id(p))  # 140706744935088 :)))
print(id(y))  # 140706744935088 :)))
print(id(t))  # 140706744935120
############
# is keyword
print(p is 10)  # True
print(y is 10)  # True
print(t is 10)  # False

############
p1 = 100000010000001000000
y1 = 100000010000001000000
print(id(p1))  # :(
print(id(y1))  # :(
print(id(100000010000001000000))  #
############
# is keyword
print(p1 is 100000010000001000000)  # False
print(y1 is 100000010000001000000)  # False

####
# python cache a little
# printed -5 and 256
for k in range(-1000, 1000):
    for v in range(-1000, 1000):
        if k is v:
            print(k)

################################################
#  example calculate
input_val = """
(1) collect
(2) take off
(3) multiply
(4) divide
Calculate square (5)
(6) calculate square root
"""
print(input_val)
# question = input("Enter the number of the action you want to do:")
question = 2
if question == "1":
    number1 = int(input("Enter the first number for addition:"))
    number2 = int(input("Enter the second number for addition:"))
    print(number1, "+", number2, "=", number1 + number2)
elif question == "2":
    number3 = int(input("Enter the first number for subtraction:"))
    number4 = int(input("Enter the second number for subtraction:"))
    print(number3, "-", number4, "=", number3 - number4)
elif question == "3":
    number5 = int(input("Enter the first number for multiplication:"))
    number6 = int(input("Enter the second number for multiplication:"))
    print(number5, "x", number6, "=", number5 * number6)
elif question == "4":
    number7 = int(input("Enter the first number for division:"))
    number8 = int(input("Enter the second number for division:"))
    print(number7, "/", number8, "=", number7 / number8)
elif question == "5":
    number9 = int(input("Enter the number whose square you want to calculate:"))
    print(number9, "square of the number =", number9 ** 2)
elif question == "6":
    number10 = int(input("Enter the number you want to calculate the square root of:"))
    print(number10, "square root of the number =", number10 ** 0.5)
else:
    print("Incorrect entry.")
    print("Enter one of the following options:", input_val)

########################################################################################
# python version 2.x and 3.x

import sys

print(sys.version_info)
print(sys.version_info.major)
print(sys.version_info.minor)
if sys.version_info.major >= 3:
    print("Python ver 3")
elif sys.version_info.major < 3:
    print("Python ver 2")
