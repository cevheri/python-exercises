# dictionary and methods

dict_1 = {}
type(dict_1)  # <class 'dict'>

translate_table = {"Ö": "O",
                   "ç": "c",
                   "Ü": "U",
                   "Ç": "C",
                   "İ": "I",
                   "ı": "i",
                   "Ğ": "G",
                   "ö": "o",
                   "ş": "s",
                   "ü": "u",
                   "Ş": "S",
                   "ğ": "g"}

dict_1 = {"kitap": "book",
          "bilgisayar": "computer",
          "programlama": "programming",
          "dil": "language",
          "defter": "notebook",
          "defter": "notebook"  # !!!!!
          }

print(dict_1["kitap"])  # book

dict_1["defter3"] = "notebook"

d = (1, 2, 3)
dict_1[d] = "python"

dict_1[1] = 1
print(dict_1)

####
# example
chars = 'abcçdefgğhıijklmnoöprsştuüvyz'
dic = {}
for c in chars:
    dic[c] = chars.index(c)
# or
d = {}
for i in range(len(chars)):
    d[chars[i]] = i
# or

d2 = {c: chars.index(c) for c in chars}
print(d2)

# example 2

d3 = {i: len(str(i)) for i in dict_1}
print(d3)
