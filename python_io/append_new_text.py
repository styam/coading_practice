"""
Write a Python program to append text in a existing file
"""

def append_text(file_name):
    with open(file_name, "a") as file:
        file.write("Django is the Python high level web framework!\n")
        file.write("and flask is also a good python framework")
    with open(file_name, "r") as read_file:
        res = [i for i in read_file]
    return res

print(append_text("append.txt"))