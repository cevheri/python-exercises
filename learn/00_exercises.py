# #----------------------------------------#

# https://edabit.com/

# Question:
#
# Write a program to solve a classic ancient Chinese puzzle:
# We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

def solve(numheads, numlegs):
    ns = 'No solutions!'
    for i in range(numheads + 1):
        j = numheads - i
        if 2 * i + 4 * j == numlegs:
            return i, j
    return ns, ns


numheads = 35
numlegs = 94
solutions = solve(numheads, numlegs)
print(solutions)
# #----------------------------------------#


listOne = [20, 20, 20, 20]
print("All element are duplicate in listOne", listOne.count(listOne[0]) == len(listOne))

listTwo = [20, 20, 20, 50]
print("All element are duplicate in listTwo", listTwo.count(listTwo[0]) == len(listTwo))

from collections import Counter

one = [33, 22, 11, 44, 55]
two = [22, 11, 44, 55, 33]
print(Counter(one))
print(Counter(two))
print("is two list are b equal", Counter(one) == Counter(two))


def isUnique(item):
    tempSet = set()
    a = any(i in tempSet or tempSet.add(i) for i in item)
    return not a


listOne = [123, 345, 456, 23, 567]
print("All List elemtnts are Unique ", isUnique(listOne))

listTwo = [123, 345, 567, 23, 567]
print("All List elemtnts are Unique ", isUnique(listTwo))


def grade_percentage(user_score, pass_score):
    s = ''
    if int(user_score[:-1]) < int(pass_score[:-1]):
        s = s + 'FAILED'
    if int(user_score[:-1]) >= int(pass_score[:-1]):
        s = s + 'PASSED'
    return 'You' + ' ' + s + ' ' + 'the Exam'


import unittest

# assert_equals(
print(grade_percentage("85%", "85%"), "You PASSED the Exam")

# print(grade_percentage("99%", "85%"), "You PASSED the Exam")
# print(grade_percentage("65%", "90%"), "You FAILED the Exam")
# print(grade_percentage("65%", "66%"), "You FAILED the Exam")
# print(grade_percentage("5%", "5%"), "You PASSED the Exam")
# print(grade_percentage("5%", "6%"), "You FAILED the Exam")
# print(grade_percentage("9%", "6%"), "You PASSED the Exam")


for i in range(3):
    print(i)


def stutter(word):
    w = ""
    for i in range(1, 3):
        w += word[0:2] + "... "
    w += word + "?"
    return w


print(stutter(("cevher")))

a = 3
import math

print(math.factorial(a))


def fact(num):
    if num < 2:
        return 1
    else:
        return num * fact(num - 1)


print(fact(a))


def fact2(num):
    v = 1
    for i in range(num + 1):
        if i > 0:
            v *= i
    return v


print(fact2(a))


def is_subset(lst1, lst2):
    s1, s2 = set(lst1), set(lst2)
    return s1.issubset(s2)


print(is_subset([3, 2, 5], [5, 3, 7, 9, 2]))
print(is_subset([8, 9], [7, 1, 9, 8, 4, 5, 6]))
print(is_subset([1, 2], [1, 2, 3]))
print(is_subset([1, 2], [3, 5, 9, 1]))
print(is_subset([1, 2, 3, 4], [4, 3, 2, 1]))
print(is_subset([7, 9, 8, 4, 2], [7, 9, 5, 8, 4]))

first, *middle, last = [1, 2, 3, 4, 5, 6]

print(first)
print(middle)
print(last)

first, *middle = [1, 2, 3, 4, 5, 6]
*middle, last = [1, 2, 3, 4, 5, 6]
last = [0, 1, 2, 3, 4, 5, 6]
print(first)
print(middle)
print(last)


def odd(number):
    return number % 2 == 1


print((filter(lambda x: x % 2 == 0, last)))

import math


#
def cone_volume(h, r):
    return round((math.pi * float(r ** 2) * h) / 3, 2)


print(cone_volume(0, 30))  # , 12.57

lst = [
    "###",
    "###",
    "###"
]

lst2 = []
ch = 0
for i in lst2:
    ch += len(i)
print(ch)


def list_operation(a, b, c):
    return [i for i in range(a, b + 1) if i % c == 0]


print(list_operation(1, 10, 3), [3, 6, 9])
print(list_operation(7, 9, 2), [8])
print(list_operation(15, 20, 7), [])
print(list_operation(10, 50, 10), [10, 20, 30, 40, 50])
print(list_operation(1, 10, 2), [2, 4, 6, 8, 10])
print(list_operation(1, 100, 17), [17, 34, 51, 68, 85])
print(list_operation(15, 20, 5), [15, 20])


def length(txt):
    if not txt:
        return 0
    else:
        return 1 + length(txt[1:])


print(length("cevher"))


def missing_letter1(lst):
    lower_alp = "abcdefghijklmnopqrstuvyz"
    upper_alp = lower_alp.upper()
    count = 0
    if lst[0].islower():
        for i in lower_alp:
            if i in lst:
                count += 1
            elif count > 0 and i not in lst:
                return i
    else:
        for i in upper_alp:
            if i in lst:
                count += 1
            elif count > 0 and i not in lst:
                return i
    return ""


def missing_letter2(lst):
    for previous, next in zip(lst, lst[1:]):
        if ord(next) - ord(previous) > 1:  # difference char
            return chr(ord(previous) + 1)


print()


def missing_letter3(lst):
    for i in lst:
        if chr(ord(i) + 1) not in lst:
            return chr(ord(i) + 1)


def missing_letter(lst):
    for i in lst:
        if chr(ord(i) + 1) not in lst:
            return chr(ord(i) + 1)


print(missing_letter(["a", "b", "c", "e", "f", "g"]), "d")
print(missing_letter(["O", "Q", "R", "S"]), "P")
print(missing_letter(["t", "u", "v", "w", "x", "z"]), "y")
print(missing_letter(["m", "o"]), "n")
print(missing_letter(
    ["a", "b", "c", "d", "e", "f", "g", "h", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
     "y", "z"]), "i")
print(missing_letter(["q", "s", "t"]), "r")
print(missing_letter(["c", "d", "e", "f", "g", "h", "i", "k", "l", "m", "n"]), "j")
print(missing_letter(["e", "f", "g", "h", "i", "j", "k", "m", "n", "o", "p"]), "l")
print(missing_letter(["t", "u", "w", "x"]), "v")
print(missing_letter(["B", "D"]), "C")


def find_nemo(ch):
    if 'Nemo' in ch.split():
        return 'I found Nemo at {}!'.format(ch.split().index('Nemo') + 1)
    return "I can't find Nemo :("


print(find_nemo("I am Ne mo Nemo !"), "I found Nemo at 5!")
print(find_nemo("N e m o is NEMO NeMo Nemo !"), "I found Nemo at 8!")
print(find_nemo("I am Nemo's dad Nemo senior ."), "I found Nemo at 5!")
print(find_nemo("Oh, hello !"), "I can't find Nemo :(")
print(find_nemo("Is it Nemos, Nemona, Nemoor or Garfield?"), "I can't find Nemo :(")
print(find_nemo("Nemo is a clown fish, he has white and orange stripes. Nemo , come back!"), "I found Nemo at 1!")

a = 50

# def f(p):
#     if p % 15 == 0:
#         s = "FizzBuzz"
#         if p % 5 == 0:
#             s = "Buzz"
#         else
#             s = "Fizz"
#     else:
#         s = str(p)
#     return p


a, b = 10, 20

if a != b:
    if a > b:
        print("a is greater than b")
    else:
        print("b is greater than a")
else:
    print("Both a and b are equal")
print()
print("3 lü")

p = 45


def f1(p):
    if p % 3 == 0 or p % 5 == 0:
        if p % 5 == 0:
            if p % 3 == 0:
                s = "FizzBuzz"
            else:
                s = "Buzz"
        else:
            s = "Fizz"
    else:
        s = str(p)
    return s


print()
print(f1(3))
print(f1(5))
print(f1(15))
print(f1(10))
print(f1(98))


def f2(p):
    if p % 3 == 0 or p % 5 == 0:
        return ("Fizz" if p % 5 != 0 else "FizzBuzz"
        if p % 3 == 0 else "Buzz")
    else:
        return str(p)


print("-" * 30)
print(f2(3))
print(f2(5))
print(f2(15))
print(f2(10))
print(f2(98))

num = 3
print("Fizz" * (num % 3 == 0))
print("Buzz" * (num % 5 == 0))
print(str(num))

ch = "cevher"
print("str".join(sorted(ch)))

str, int = int, str

if str(4) == '4' and int('4') == 4:
    print('**EXTRA POINTS**')
    print('You have successfully de-drunken Python')

str, int = int, str


def int_to_str(num):
    str(num)


def str_to_int(num):
    int(num)


print(int_to_str(4), '4')
print(int_to_str(65), '65')
print(int_to_str(29348), '29348')
print(int_to_str(49583908545), '49583908545')

print(str_to_int('4'), 4)
print(str_to_int('65'), 65)
print(str_to_int('29348'), 29348)
print(str_to_int('49583908545'), 49583908545)

n = 43365644
lst = [int(d) for d in str(n)]
[4, 3, 3, 6, 5, 6, 4, 4]

print(sum(lst))


def is_equal(lst):
    # [1,1]
    l0 = lst[0] % 9  # [int(i) for i in str(lst[0])]

    # [2,0]
    l1 = lst[1] % 9  # [int(i) for i in str(lst[0])]
    return sum(l0) == sum(l1)


# print(is_equal([14, 21]))
import math

print(str(-9).isdigit())


def f(l):
    return [i for i in l if isinstance(i, int)]


print(f([1, 2, -9, 0, "1", "h", "q"]))


def add_indexes(lst2):
    l = []
    for i, v in enumerate(lst2):
        a = i
        b = v
        l.append(i + v)
    return l


def add_indexes2(lst2):
    return [i + v for i, v in enumerate(lst2)]


# return [i + enumerate(lst,i) for i in lst]


print(add_indexes2([0, 0, 0, 0, 0]))  # ➞ [0, 1, 2, 3, 4]

print(add_indexes2([1, 2, 3, 4, 5]))  # ➞ [1, 3, 5, 7, 9]

print(add_indexes2([5, 4, 3, 2, 1]))  # ➞ [5, 5, 5, 5, 5]

import re

lst = ['bad cookie', 'good cookie', 'bad cookie', 'good cookie', 'good cookie']

pattern = "(?<!cookie)bad"
print('(?<!' in pattern, True, 'You must use negative lookbehind.')
st = ', '.join(lst)
print(st)
print(len(re.findall(pattern, st)), 2)
print(re.findall(pattern, st))


#####################################################################################3
def encode_morse(message):
    char_to_dots = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
        ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
        '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
    }

    print()
    message_split = [_ for _ in message.upper()]
    print(message_split)
    print()
    morse_list = []
    for number, value in enumerate(message_split):
        morse_list.append(char_to_dots[value])
    print()
    print(morse_list)
    return ' '.join(morse_list)


# print(encode_morse("EDABBIT CHALLENGE"), "|",". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. .", "Test 1")

# print(encode_morse("HELP ME !"), "|||", ".... . .-.. .--.   -- .   -.-.--", "Test 2")
# print(encode_morse("CHALLENGE"), "|||", "-.-. .... .- .-.. .-.. . -. --. .", "Test 3")
# print(encode_morse("1 APPLE AND 5 CHERRY, 7 SANDWICHES, 2 TABLES, 9 INVITED GUYS ! THAT'S SO COOL..."), "|||", ".----   .- .--. .--. .-.. .   .- -. -..   .....   -.-. .... . .-. .-. -.-- --..--   --...   ... .- -. -.. .-- .. -.-. .... . ... --..--   ..---   - .- -... .-.. . ... --..--   ----.   .. -. ...- .. - . -..   --. ..- -.-- ...   -.-.--   - .... .- - .----. ...   ... ---   -.-. --- --- .-.. .-.-.- .-.-.- .-.-.-", "Test 4")
print(encode_morse("did you got my mail ?"), "|||",
      "-.. .. -..   -.-- --- ..-   --. --- -   -- -.--   -- .- .. .-..   ..--..", "Test 5")
# print(encode_morse("TWO THInGS TO KNOW : i FORGeT THeM :C"), "|||", "- .-- ---   - .... .. -. --. ...   - ---   -.- -. --- .--   ---...   ..   ..-. --- .-. --. . -   - .... . --   ---... -.-.", "Test 6")
################################################
import datetime


def has_friday_13(month, year):
    d = datetime.datetime(year, month, 13)
    return d.strftime("%A") == "Friday"


print(has_friday_13(3, 2020), True)
print(has_friday_13(10, 2017), True)
print(has_friday_13(1, 1985), False)
print(has_friday_13(5, 1619), False)
print(has_friday_13(6, 1614), True)
print(has_friday_13(8, 1767), False)
print(has_friday_13(6, 1589), False)
print(has_friday_13(2, 2015), True)
print(has_friday_13(3, 2015), True)
print(has_friday_13(11, 2015), True)
print(has_friday_13(2, 1759), False)
print(has_friday_13(8, 1612), False)
print(has_friday_13(8, 1612), False)
print(has_friday_13(10, 2029), False)
print(has_friday_13(1, 1590), False)
print(has_friday_13(7, 1812), False)
print(has_friday_13(1, 1785), False)
print(has_friday_13(11, 1961), False)
print(has_friday_13(9, 1706), False)
print(has_friday_13(5, 2016), True)
print(has_friday_13(11, 2020), True)
print(has_friday_13(1, 2023), True)
print(has_friday_13(10, 2023), True)
print(has_friday_13(2, 2043), True)
print(has_friday_13(4, 2043), False)
print(has_friday_13(3, 2043), True)
print(has_friday_13(11, 2043), True)
