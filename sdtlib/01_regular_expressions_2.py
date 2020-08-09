# matching object methods


# group() with parentheses
import re

text = "Python is a powerful programming language"
keyword = ("(Python) (is) (a)")
match = re.search(keyword, text)
print(match.group())
print(match.group(0))
print(match.group(1))
print(match.group(2))
print(match.group(3))

print(match.groups())

import re
from urllib.request import urlopen

url = "https://web.archive.org/web/20121025012131/http://www.istihza.com/py2/icindekiler_python.html"
f = urlopen(url)

çıktı = "Başlık: {};\nBağlantı: {}\n"
regex = 'href="(.+html)">(.+)</a>'

for i in f:
    nesne = re.search(regex, str(i, 'utf-8'))
    if nesne:
        print(nesne.groups())
###################################################
print()
## space \s
print("space \s")

a = ["5 Ocak", "27Mart", "4 Ekim", "Nisan 3"]
for i in a:
    m = re.search("[0-9]\\s[A-Za-z]+", i)
    if m:
        print(m.group())
# 5 Ocak
# 4 Ekim
###################################################
print()
## float \d
print("float \d")
a = ["5 Ocak", "27Mart", "4 Ekim", "Nisan 3"]
for i in a:
    m = re.search("\d\s[A-Za-z]+", i)
    if m:
        print(m.group())
# 5 Ocak
# 4 Ekim
###################################################
print()
## alphanumeric \w
# \w = [A-Za-z0-9_]
print("alphanumeric \w")

a = "abc123_$%+"
print(re.search("\w*", a).group())
# abc123_
#################################
# \s = space;        \S = not space
# \d = float;        \D = not float
# \w = alphanumeric; \W = not alphanumeric
a = ["5 Ocak", "27Mart", "4 Ekim", "Nisan 3"]
for i in a:
    m = re.search("\d+\S\w+", i)
    if m:
        print(m.group())
# 27Mart
#################################################
# example
text = ["esra : istinye 05331233445"
    , "esma : levent 05322134344 "
    , "sevgi : dudullu 05354445434 "
    , "kemal : sanayi 05425455555 "
    , "osman : tahtakale 02124334444"
    , "metin : taksim "
    , "kezban : caddebostan 02163222122"]
# isim > telefon numarası

for i in text:
    match = re.search("(\w+)\s+:\s(\w+)\s+(\d+)", i)
    if match:
        print(match.groups())
        # print(match.group(1), match.group(3))

# https://web.archive.org/web/20130511050633/http://www.istihza.com/denemeler/yigin.txt
# decrypt

#################################################
# compile() IGNORECASE
print("compile()")
l = ["Python2.7", "Python3.2", "Python3.3", "python3.4", "Java"]
comp = re.compile("[A-Za-z]+[0-9]\.[0-9]")
for i in l:
    m = comp.search(i)
    if m:
        print(m.group())

text = """Programlama dili, programcının bir bilgisayara ne yapmasını
istediğini anlatmasının standartlaştırılmış bir yoludur. Programlama
dilleri, programcının bilgisayara hangi veri üzerinde işlem yapacağını,
verinin nasıl depolanıp iletileceğini, hangi koşullarda hangi işlemlerin
yapılacağını tam olarak anlatmasını sağlar. Şu ana kadar 2500’den fazla
programlama dili yapılmıştır. Bunlardan bazıları: Pascal, Basic, C, C#,
C++, Java, Cobol, Perl, Python, Ada, Fortran, Delphi programlama
dilleridir."""
print()
print("compile() > re.IGNORECASE or r.I")
c = re.compile("programlama", re.IGNORECASE)
c = re.compile("programlama", re.I)
print(c.findall(text))
print()

####
# re.DOTALL veya re.S¶
print("compile > re.DOTALL or re.S")

a = "Ben Python,\nMonty Python"
comp = re.compile("Python.*", re.DOTALL)
match= comp.search(a)
print(match.group())
#comp = re.compile("Python.*", re.S)

print()
####
# sub() methods
print("sub() methods")

a = "Kırmızı başlıklı kız, kırmızı elma dolu sepetiyle \
anneannesinin evine gidiyormuş!"
c = re.compile("kırmızı", re.IGNORECASE)
print(c.sub("yeşil", a))
# yeşil başlıklı kız, yeşil elma dolu sepetiyle anneannesinin evine gidiyormuş!
####################
print()
text = """Karadeniz Ereğlisi denince akla ilk olarak kömür ve demir-çelik
gelir. Kokusu ve tadıyla dünyaya nam salmış meşhur Osmanlı çileği ise ismini
verdiği festival günleri dışında pek hatırlanmaz. Oysa Çin'den Arnavutköy'e
oradan da Ereğli'ye getirilen kralların meyvesi çilek, burada geçirdiği değişim
sonucu tadına doyulmaz bir hal alır. Ereğli'nin havasından mı suyundan mı
bilinmez, kokusu, tadı bambaşka bir hale dönüşür ve meşhur Osmanlı çileği
unvanını hak eder. Bu nazik ve aromalı çilekten yapılan reçel de likör de bir
başka olur. Bu yıl dokuzuncusu düzenlenen Uluslararası Osmanlı Çileği Kültür
Festivali'nde 36 üretici arasında yetiştirdiği çileklerle birinci olan Kocaali
Köyü'nden Güner Özdemir, yılda bir ton ürün alıyor. 60 yaşındaki Özdemir,
çileklerinin sırrını yoğun ilgiye ve içten duyduğu sevgiye bağlıyor: "Erkekler
bahçemize giremez. Koca ayaklarıyla ezerler çileklerimizi" Çileği toplamanın zor
olduğunu söyleyen Ayşe Özhan da çocukluğundan bu yana çilek bahçesinde
çalışıyor. Her sabah 04.00'te kalkan Özhan, çileklerini özenle suluyor. Kasım
başında ektiği çilek fideleri haziran başında meyve veriyor."""
# çilek > erik
# çileği > eriği
comp = re.compile("çile[kğ]", re.IGNORECASE)

def change(match):
    a = {"çileğ":"eriğ", "Çileğ":"Eriğ", "Çilek":"Erik", "çilek":"erik"}
    b = match.group().split()
    for i in b:
        return a[i]

print(comp.sub(change, text))


print()
####
# subn() methods
print("subn() methods")
print(comp.subn(change, text)[1])