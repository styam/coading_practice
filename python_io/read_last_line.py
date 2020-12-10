"""
Write a Python program to append text to a file and display the text
"""

def read_last_line(file_name):
    with open(file_name, "r") as file:
        res = [i for i in file[::-1]]
    return res.read