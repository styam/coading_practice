"""
Write a Python program to read a file line by line and store it into a list.
"""

def read_line_by_line(file_name):
    with open(file_name) as file:
        content_list = file.readline()
    return content_list

print(read_line_by_line("main.txt"))