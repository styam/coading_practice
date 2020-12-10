"""
Python Program to Remove Given Key from a Dictionary.
"""


def remove_given_key():
    d = {"name": "Satyam", "age": 26, "address": "Bangalore"}
    key = input("Enter your key\n")
    if key in d.keys():
        # d.pop(key)
        del d[key]
    else:
        return "Given key is not in dict"
    return d


print(remove_given_key())
