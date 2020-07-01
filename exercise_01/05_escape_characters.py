# escape characters

# backslash \
print("Python is a \"script\" language. ")  # Python is a "script" language.

################################################
# newline \n
print("Python is \n a script language.")
# Python is
#  a script language.

info = "Python is a script language"
print(info, "\n", "-" * len(info), sep="")
# Python is a script language
# ---------------------------
# bad
print("c:\neo\text.txt")
# c:
# eo	ext.txt

# good
print("c:\\neo\\text.txt")
# c:\neo\text.txt

print("c:/neo/text.txt")
# c:/neo/text.txt

################################################
# tab \t
# bad
print("c:\text.txt")
# c:	ext.txt

# good
print("c:\\text.txt")
# c:\text.txt

print("one", "two", "tree", sep="\t")
# one	two     tree
################################################
# bip \a
print("\a")  # biiip

################################################
# \r is a carriage return character
print("Python is a \rscript language. ")
# script language.

# \v
print("Python is a \v script language. ")  # dont work win

# \b
print("Python is a\bscript language.")  # Python is script language.

print("python", ".", "org")  # python . org
print("python", ".", "org", sep="")  # python.org
print("python", "\b.", "\borg")  # python.org

################################################
# unicode escape \u
print("\u0061")  # a

print("c:\\users\\cevher")  # \\u !!!!!

# hexadecimal \x
print("\x66")  # f

# r key
print(r"c:\user\cevher")  # r"... !!!

# error
# print(r"Python \")

# Kaçış Dizisi	Anlamı
# \’	Karakter dizisi içinde tek tırnak işaretini kullanabilmemizi sağlar.
#
# \”	Karakter dizisi içinde çift tırnak işaretini kullanabilmemizi sağlar.
#
# \\	Karakter dizisi içinde
# 	\ işaretini kullanabilmemizi sağlar.
#
# \n	Yeni bir satıra geçmemizi sağlar.
#
# \t	Karakterler arasında sekme boşluğu bırakmamızı sağlar.
#
# \u	UNICODE kod konumlarını gösterebilmemizi sağlar.
#
# \U	UNICODE kod konumlarını gösterebilmemizi sağlar.
#
# \N	Karakterleri UNICODE adlarına göre kullanabilmemizi sağlar.
#
# \x	Onaltılı sistemdeki bir sayının karakter karşılığını gösterebilmemizi sağlar.
#
# \a	Destekleyen sistemlerde, kasa hoparlöründen bir ‘bip’ sesi verilmesini sağlar.
#
# \r	Aynı satırın başına dönülmesini sağlar.
#
# \v	Destekleyen sistemlerde düşey sekme oluşturulmasını sağlar.
#
# \b	İmlecin sola doğru kaydırılmasını sağlar
#
# \f	Yeni bir sayfaya geçilmesini sağlar.
#
# r	Karakter dizisi içinde kaçış dizilerini kullanabilmemizi sağlar.
# ref: https://python-istihza.yazbel.com/kacis_dizileri.html
