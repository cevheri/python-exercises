# file methods

# open()
# create file
# delete and new file
open("26_first_text.txt", "w")

f = open("26_first_text.txt", "w")
f.close()

# write() file
f = open("26_first_text.txt", "w")
val = """First Line
Second Line
Third Line
"""
f.write(val)
f.close()

# read(), readline(), readlines()
f = open("26_first_text.txt")  # or f = open("26_first_text.txt", "r")
print(f.read())
# First Line
# Second Line
# Third Line
f.close()

f = open("26_first_text.txt")  # or f = open("26_first_text.txt", "r")
print(f.readline())  # First Line
print(f.readline())  # Second Line
print(f.readline())  # Third Line
print(f.readline())  # null
f.close()

####################################
# file closed
try:
    f = open("26_first_text.txt")  # or f = open("26_first_text.txt", "r")
    print(f.readlines())  # ['First Line\n', 'Second Line\n', 'Third Line\n']
except IOError:
    print("Error")
finally:
    f.close()

# file closed
with open("26_first_text.txt") as f:
    print(f.read())

# re-read
with open("26_first_text.txt") as f:
    print(f.read())
    f.seek(0)
    print(f.read())
    print(f.tell())

# file add()
with open("26_first_text2.txt", "a") as a:
    a.write("First Line\n")

with open("26_first_text.txt", "r+") as a:
    data = a.read()
    a.seek(0)
    a.write("Start Line\n" + data)

with open("26_first_text.txt", "r+") as f:
    data = f.readlines()
    data.insert(2, "Start Line (readlines and writelines)\n")
    f.seek(0)
    f.writelines(data)

# Kip Açıklaması
#
# "r"
# Bu öntanımlı kiptir. Bu kip dosyayı okuma yetkisiyle açar. Ancak bu kipi kullanabilmemiz için, ilgili dosyanın disk üzerinde halihazırda var olması gerekir. Eğer bu kipte açılmak istenen dosya mevcut değilse Python bize bir hata mesajı gösterecektir. Dediğimiz gibi, bu öntanımlı kiptir. Dolayısıyla dosyayı açarken herhangi bir kip belirtmezsek Python dosyayı bu kipte açmak istediğimizi varsayacaktır.
#
# "w"
# Bu kip dosyayı yazma yetkisiyle açar. Eğer belirttiğiniz adda bir dosya zaten disk üzerinde varsa, Python hiçbir şey sormadan dosya içeriğini silecektir. Eğer belirttiğiniz adda bir dosya diskte yoksa, Python o adda bir dosyayı otomatik olarak oluşturur.
#
# "a"
# Bu kip dosyayı yazma yetkisiyle açar. Eğer dosya zaten disk üzerinde mevcutsa içeriğinde herhangi bir değişiklik yapılmaz. Bu kipte açtığınız bir dosyaya eklediğiniz veriler varolan verilere ilave edilir. Eğer belirttiğiniz adda bir dosya yoksa Python otomatik olarak o adda bir dosyayı sizin için oluşturacaktır.
#
# "x"
# Bu kip dosyayı yazma yetkisiyle açar. Eğer belirttiğiniz adda bir dosya zaten disk üzerinde varsa, Python varolan dosyayı silmek yerine size bir hata mesajı gösterir. Zaten bu kipin “w” kipinden farkı, varolan dosyaları silmemesidir. Eğer belirttiğiniz adda bir dosya diskte yoksa, bu kip yardımıyla o ada sahip bir dosya oluşturabilirsiniz.
#
# "r+"
# Bu kip, bir dosyayı hem yazma hem de okuma yetkisiyle açar. Bu kipi kullanabilmeniz için, belirttiğiniz dosyanın disk üzerinde mevcut olması gerekir.
#
# "w+"
# Bu kip bir dosyayı hem yazma hem de okuma yetkisiyle açar. Eğer dosya mevcutsa içerik silinir, eğer dosya mevcut değilse oluşturulur.
#
# "a+"
# Bu kip bir dosyayı hem yazma hem de okuma yetkisiyle açar. Eğer dosya zaten disk üzerinde mevcutsa içeriğinde herhangi bir değişiklik yapılmaz. Bu kipte açtığınız bir dosyaya eklediğiniz veriler varolan verilere ilave edilir. Eğer belirttiğiniz adda bir dosya yoksa Python otomatik olarak o adda bir dosyayı sizin için oluşturacaktır.
#
# "x+"
# Bu kip dosyayı hem okuma hem de yazma yetkisiyle açar. Eğer belirttiğiniz adda bir dosya zaten disk üzerinde varsa, Python varolan dosyayı silmek yerine size bir hata mesajı gösterir. Zaten bu kipin “w+” kipinden farkı, varolan dosyaları silmemesidir. Eğer belirttiğiniz adda bir dosya diskte yoksa, bu kip yardımıyla o ada sahip bir dosya oluşturup bu dosyayı hem okuma hem de yazma yetkisiyle açabilirsiniz.
#
# "rb"
# Bu kip, metin dosyaları ile ikili (binary) dosyaları ayırt eden sistemlerde ikili dosyaları okuma yetkisiyle açmak için kullanılır. “r” kipi için söylenenler bu kip için de geçerlidir.
#
# "wb"
# Bu kip, metin dosyaları ile ikili dosyaları ayırt eden sistemlerde ikili dosyaları yazma yetkisiyle açmak için kullanılır. “w” kipi için söylenenler bu kip için de geçerlidir.
#
# "ab"
# Bu kip, metin dosyaları ile ikili dosyaları ayırt eden sistemlerde ikili dosyaları yazma yetkisiyle açmak için kullanılır. “a” kipi için söylenenler bu kip için de geçerlidir.
#
# "xb"
# Bu kip, metin dosyaları ile ikili dosyaları ayırt eden sistemlerde ikili dosyaları yazma yetkisiyle açmak için kullanılır. “x” kipi için söylenenler bu kip için de geçerlidir.
#
# "rb+"
# Bu kip, metin dosyaları ile ikili dosyaları ayırt eden sistemlerde ikili dosyaları hem okuma hem de yazma yetkisiyle açmak için kullanılır. “r+” kipi için söylenenler bu kip için de geçerlidir.
#
# "wb+"
# Bu kip, metin dosyaları ile ikili dosyaları ayırt eden sistemlerde ikili dosyaları hem okuma hem de yazma yetkisiyle açmak için kullanılır. “w+” kipi için söylenenler bu kip için de geçerlidir.
#
# "ab+"
# Bu kip, metin dosyaları ile ikili dosyaları ayırt eden sistemlerde ikili dosyaları hem okuma hem de yazma yetkisiyle açmak için kullanılır. “a+” kipi için söylenenler bu kip için de geçerlidir.
#
# "xb+"
# Bu kip, metin dosyaları ile ikili dosyaları ayırt eden sistemlerde ikili dosyaları hem okuma hem de yazma yetkisiyle açmak için kullanılır. “x+” kipi için söylenenler bu kip için de geçerlidir.


