"""
Python program to filter a dictionary based on values

{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
Marks greater than 170:
{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}

"""


def filter_by_value(marks):
    # marks = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
    result = {key:value for (key, value) in marks.items() if value >= 170}
    print(f"Original dict is {marks}")
    return result

marks = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
print(filter_by_value(marks))
