import os
import keyword
import sys

print("Current file directory:", os.getcwd())
print("Python Keyword List:", keyword.kwlist)
print(sys.stdout)

output_file = open("output/print_output_file.txt", "w")
print("Python print output example 1", file=output_file)  # flush=False
output_file.close()

# with flush true
output_file_flush = open("output/print_output_file_flush.txt", "w")
print("Python print output example 1",
      file=output_file_flush,
      flush=True)
# output_file_flush.close()

# Practice
# bad
print("L", "i", "n", "u", "x", sep=".")
# good
print(*"Linux", sep=".")
print(*"Manjaro")

# stdout file >> make permanent
per_file = open("output/stdout.log", "w")
sys.stdout, orj_stdout = per_file, sys.stdout
print("stdout log", flush=True)
print(sys.stdout, flush=True)  # <_io.TextIOWrapper name='./output/stdout.log' mode='w' encoding='cp1254'>

# undo sys.stdout
sys.stdout = orj_stdout
print("log stdout")
