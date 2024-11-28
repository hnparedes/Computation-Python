# 1ab
# basic file write
# filename = input("Enter filename: ")
# content_ = "This is a test\n"

# try:
#     outfile = open(filename, "w")
#     try:
#         outfile.write(content_)
#     finally:
#         outfile.close()
# except FileNotFoundError as e:
#     print(f"exception occurred as : ", e)
# finally:
#     print("Continue with program")

# use_pathlib.py
from pathlib import Path
data_folder = Path("../data/text.d/")
file_to_open = data_folder / "some_text.txt"
print(file_to_open.read_text())
# read_text function should not be used for large files
