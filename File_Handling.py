# Programs can create file, read file, write data into files.
# Without file handling: programs lose data after closing.
# File is used for reports, logs, transaction records, analytics, saved appliation dats.
# "r" - read mode, "w" - write mode, "a" - append mode, "x" - create mode.
# "r+" - read and write mode, "w+" - write and read mode, "a+" - append and read mode, "x+" - create and read mode.
file = open("data.text", "w") # creates a file named data.text in write mode
file.write("Hello Python")
file.close() # Always close file after use.

file = open("data.text", "w")
file.write("Machine Running Normally")
file.close()

file = open("data.text", "r")
content = file.read()
print (content)
file.close()

file = open("data.text", "a")
file.write("\nNew temperature added")
file.close()