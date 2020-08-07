# String Methods

# str.maketrans(), translate()
# isalpha()
# isdigit()
# isalnum()
# isdecimal()
# isidentifier()
# isnumeric()
# isspace()
# isprintable()

# 1- str.maketrans(), translate()¶
source = "şçöğüıŞÇÖĞÜİ"
target = "scoguiSCOGUI"
translate_table = str.maketrans(source, target)
text_val = "PİTON proğramlama DİLİ işleme çalışması"
print(text_val.translate(translate_table))
# PITON programlama DILI isleme calismasi
print('-' * 30)

q_keyboard = "qwertyuıopğüasdfghjklşi,zxcvbnmöç."
f_keyboard = "fgğıodrnhpqwuieaütkmlyşxjövcçzsb.,"
q_f_keybord_dic = {"q": "f", "w": "g", "e": "ğ", "r": "ı", "t": "o", "y": "d", "u": "r",
                   "ı": "n", "o": "h", "p": "p", "ğ": "q", "ü": "w", "a": "u", "s": "i",
                   "d": "e", "f": "a", "g": "ü", "h": "t", "j": "k", "k": "m", "l": "l",
                   "ş": "y", "i": "ş", ",": "x", "z": "j", "x": "ö", "c": "v", "v": "c",
                   "b": "ç", "n": "z", "m": "s", "ö": "b", "ç": ".", ".": ","}
############################################
# isalpha(), isdigit(), isalnum(), isdecimal()

print("CEVHERİŞĞÜİÇÖİ".isalpha())  # True
print("cevheri1".isalpha())  # False

print("1234567890".isdigit())  # True
print("1234567890.".isdigit())  # False

print("1cevheri2".isalnum())  # True
print("1cevheri2.".isalnum())  # False

print("1234567890".isalnum())  # True
print("1234.567890.".isalnum())  # False
print('-' * 30)
############################################
# isidentifier() variable, func name
print("1a".isidentifier())  # False
print("a1".isidentifier())  # True
print('-' * 30)
############################################
# isnumeric()
print("12".isnumeric())  # True

print("dasd".isnumeric())  # False
print('-' * 30)
############################################
# isspace()
print(" ".isspace())  # True

print("              ".isspace())  # True

print("".isspace())  # False !!!!!!!!
print('-' * 30)
############################################
# isprintable() (non-printing characters)
# http://www.asciitable.com/
print("\n".isprintable())  # False


input_val = "qwertyuıopğüasdfghjklşizxcvbnmQWERTYUIOPĞÜASDFGHJKLŞİZXCVBNM1234567890"
rot13 =     "djreglhıbcğünfqstuwxyşvmkpioazDJREGLHIBCĞÜNFqSTUWXYŞVMKPİOAZ0987654321"

encrypt = str.maketrans(input_val, rot13)

text = input("input password '(Rot 13 password)': ")

print(text.translate(encrypt))
