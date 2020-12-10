"""
You have list of json you need to convert it into python objects and if a user entered a key
then that key should be removed from the given json
"""
import json

def remove_given_key():
    key = input("Enter your key which you want to delete\t")
    with open("students.json") as file:
        data = json.load(file)
    for name in data['students']:
        if key in name:
            # name.pop(key)
            del name[key]
    with open("new_student_data.json", "w") as new_file:
        json.dump(data, new_file, indent=4)
    return data


print(remove_given_key())
