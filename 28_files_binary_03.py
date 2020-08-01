# file methods
# closed
# readable()
# writable()
# truncate()
# mode
# name
# encoding


f = open("27_files_02.txt", "w")
print(*[m for m in dir(f) if not m.startswith("_")], sep="\n")

# or

f = open("27_files_02.txt", "w")
for m in dir(f):
    if not m.startswith("_"):
        print(m, "\n")

# buffer
# close
# closed
# detach
# encoding
# errors
# fileno
# flush
# isatty
# line_buffering
# mode
# name
# newlines
# read
# readable
# readline
# readlines
# reconfigure
# seek
# seekable
# tell
# truncate
# writable
# write
# write_through
# writelines


f.closed

f.readable()

f.writable()

# f.truncate()
with open("27_files_02.txt", "r+") as f:
    f.readline()
    f.seek(f.tell())
    f.truncate()

f=open("27_files_02.txt", "r+")
f.mode

f.name

f.encoding # 'utf-8'
f.encoding # 'cp1254' #Windows
