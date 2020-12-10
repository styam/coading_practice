"""
Write a Python program to sort (ascending and descending) a dictionary by value.
"""

import operator

d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
ascending_by_value = sorted(d.items(), key=operator.itemgetter(1))
descending_by_value = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
print(f"Dict after sorting in ascending order by value {ascending_by_value}")
print(f"Dict after sorting in descending order by value {descending_by_value}")