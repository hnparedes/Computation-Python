# 1a
try:
    filename = input("Enter filename: ")
    infile = open(filename, "r")
    line = infile.readline()
    value = int(line)

# 1b
except IOError:
    print("Error: file not found.")
except ValueError as exception:
    print("Error:", str(exception))

# 2
# filename = input("Enter filename: ")
# outfile = open(filename, "w")
# content_ = "This is a test\n"
# try:
#     outfile.write(content_)
# finally:
#     outfile.close()
