"""
Write a Python program to read first n lines of a file.
"""
from itertools import islice

def read_line_numbers(file_name, line_no):
    with open(file_name) as file:
        for line in islice(file, line_no):
            print(line)


read_line_numbers("main.txt", 2)