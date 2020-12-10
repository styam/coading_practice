"""
Write a Python program to append text to a file and display the text.
"""

def append_text(file_name):
    with open(file_name, "w") as file:
        file.write("Python is a good programing language")
        file.write()
    with open(file_name) as f:
        print(f.read())
    return file

print(append_text("text.txt"))