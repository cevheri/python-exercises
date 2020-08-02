# binary files

# f = open("28.file", 'rb')


f = open("./output/Java_Design_Pattern_eBook.pdf", "rb")
r = f.read()
producer_index= r.index(b"/Producer")
print(producer_index) # 1747002
print(r[producer_index]) # 47
print(chr(r[producer_index])) # /
print(r[producer_index:producer_index+100]) # b'/Producer 1478 0 R /Creator\n1481 0 R /CreationDate 1482 0 R /ModDate 1482 0 R >>\nendobj\nxref\n0 1483\n'
print(r[producer_index:producer_index+100].split()) # [b'/Producer', b'1478', b'0', b'R', b'/Creator', b'1481', b'0', b'R', b'/CreationDate', b'1482', b'0', b'R', b'/ModDate', b'1482', b'0', b'R', b'>>', b'endobj', b'xref', b'0', b'1483']


# jpeg
# https://jpeg.org/
# http://www.faqs.org/faqs/jpeg-faq/part1/section-15.html

# FF D8 FF E0 ? ? 4A 46 49 46 00
# FF D8 FF E0 ? ? 45 78 69 66 00 #canon

# 255 216 255 224 ? ? 74 70 73 70 0
# 255 216 255 224 ? ? 45 78 69 66 0 #canon

# J , F , I , F
# 74, 70, 73, 70
#----------------------
# E , x , i , f
# 45, 78, 69, 66 #canon

f = open("./output/jpeg_file.jpeg", 'rb')
data = f.read(10)
if data[6:11] in [b"JFIF", b"Exif"]:
    print("Is PEG!")
else:
    print("Not JPEG!")


files = ["d1.jpg", "d2.jpg", "d3.jpeg"]
for f in files:
    data = open(f, 'rb').read(10)
    print(data)
# d1.jpg         b'\xff\xd8\xff\xe0\x00\x10JFIF'
# d2.jpg         b'\xff\xd8\xff\xe1T\xaaExif'
# d3.jpeg        b'\xff\xd8\xff\xe0\x00\x10JFIF'


# PNG
# http://www.libpng.org/pub/png/spec/ : Portable Network Graphics (PNG) Specification and Extensions
# http://www.fileformat.info/format/png/egff.htm : PNG File Format Summary
# http://www.libpng.org/pub/png/spec/1.2/PNG-Rationale.html#R.PNG-file-signature : PNG file signature

# file first 8 bayt
# num : 137 80 78 71 13 10 26 10
# hex : 89 50 4e 47 0d 0a 1a 0a
# chr : \211 P N G \r \n \032 \n

# example
f = open("./output/text.png", "rb")
data = f.read(8)
print(data) # b'\x89PNG\r\n\x1a\n'

print(b'\x89PNG\r\n\x1a\n' == b'\211PNG\r\n\032\n') # True === PNG

# example, jpeg or png
files = []
for f in files:
    data = open(f, 'rb').read(10)
    if data[6:11] in [b'JFIF', b'Exif']:
        print("{} file is JPEG!".format(f))
    elif data[:8] == b"\211PNG\r\n\032\n":
        print("{} file is PNG!".format(f))
    else:
        print("Unknown type file: {}".format(f))


# GIF GRAPHICS INTERCHANGE FORMAT (1987,1988,1989,1990)
# https://www.w3.org/Graphics/GIF/spec-gif89a.txt : Cover Sheet for the GIF89a Specification
#
# start: GIF
# 87a - 1987 ‘GIF87a’
# 89a - 1989 ‘GIF89a’

# example, jpeg, png, gif
files = []
for f in files:
    data = open(f, 'rb').read(10)
    if data[6:11] in [b"JFIF", b"Exif"]:
        print("{} file is JPEG!".format(f))
    elif data[:8] == b"\211PNG\r\n\032\n":
        print("{} file is PNG!".format(f))
    elif data[:3] == b'GIF':
        print("{} file is GIF".format(f))
    else:
        print("Unknown type file: {}".format(f))

# TIFF
# https://partners.adobe.com/public/developer/en/tiff/TIFF6.pdf
# start: ‘II’ ‘MM’
# example, jpeg, png, gif, TIFF
files = []
for f in files:
    data = open(f, 'rb').read(10)
    if data[6:11] in [b"JFIF", b"Exif"]:
        print("{} file is JPEG!".format(f))
    elif data[:8] == b"\211PNG\r\n\032\n":
        print("{} file is PNG!".format(f))
    elif data[:3] == b"GIF":
        print("{} file is GIF".format(f))
    elif data[:2] in [b"II", b"MM"]:
        print("{} file is TIFF".format(f))
    else:
        print("Unknown type file: {}".format(f))

# BMP
# https://www.loc.gov/preservation/digital/formats/fdd/fdd000189.shtml
# start: BM
# example, jpeg, png, gif, TIFF, BMP
files = []
for f in files:
    data = open(f, 'rb').read(10)
    if data[6:11] in [b"JFIF", b"Exif"]:
        print("{} file is JPEG!".format(f))
    elif data[:8] == b"\211PNG\r\n\032\n":
        print("{} file is PNG!".format(f))
    elif data[:3] == b"GIF":
        print("{} file is GIF".format(f))
    elif data[:2] in [b"II", b"MM"]:
        print("{} file is TIFF".format(f))
    elif data[:2] in [b"BM"]:
        print("{} file is BMP".format(f))
    else:
        print("Unknown type file: {}".format(f))



