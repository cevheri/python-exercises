import os

output_file = open("print_output_file.txt", "w")
print("Python print output example", file=output_file)
output_file.close()
print("Current file directory:", os.getcwd())
