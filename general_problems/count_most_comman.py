"""
Write a Python program to count the most common words in a dictionary.
"""

from collections import Counter


def count_most_common_words(lst):
    words_count = Counter(lst)
    top_words = words_count.most_common(4)
    return top_words


words = [
   'red', 'green', 'black', 'pink', 'black', 'white', 'black', 'eyes',
   'white', 'black', 'orange', 'pink', 'pink', 'red', 'red', 'white', 'orange',
   'white', "black", 'pink', 'green', 'green', 'pink', 'green', 'pink',
   'white', 'orange', "orange", 'red'
]
print(count_most_common_words(words))