"""
Write a Python program to read an entire text file.
"""
def read_entire_file(file_name):
    with open(file_name) as file:
        return [i for i in file]

print(read_entire_file("main.txt"))