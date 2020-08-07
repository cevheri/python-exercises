# While Loops
# While loops, like the ForLoop, are used for repeating sections of code - but unlike a for loop,
# the while loop will not run n times, but until a defined condition is no longer met.
# If the condition is initially false, the loop body will not be executed at all.

# while True:
#     pass

p = 1
while p < 10:  # python 3.8 (p:=1)
    print("value :", p)
    p += 1

a = 0
while a < 10:
    a += 1
    if a % 2 == 0:
        print(a)

###################################
# calculate while example
entry = """
(1) collect
(2) take off
(3) multiply
(4) divide
(5) Calculate square 
(6) calculate square root
"""

print(entry)
# key = 1
while True:  # key == 1:
    question = input("Enter the number of the action you want to do (q to quit) :")

    if question == "q":
        print("Exiting ...")
        # key = 0
        break

    elif question == "1":
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
        print("Enter one of the following options:", entry)

