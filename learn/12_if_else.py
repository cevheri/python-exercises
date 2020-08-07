# if:  elif:  else:


val1 = 100
val2 = 90

# if condition
if val1 > val2:
    print("{} > {}".format(val1, val2))

val1 = 100
val2 = 190
# if else condition
if val1 > val2:
    print("{} > {}".format(val1, val2))
elif val2 > val1:
    print("{} > {}".format(val2, val1))
else:
    print("Null !!!!!")

#########################################
username = input("User Name:\t")
password = input("Password:\t")
max_length = 40
text_length = len(username) + len(password)

message = "Username and password is {} length"
print(message.format(text_length))

if text_length > max_length:
    print("Username and password length is greater than  {}".format(max_length))
else:
    print("Welcome")
