"""
Python program to calculate number of digit in a number
"""


# Through Recursive call
# def calculate_no_of_digit(num):
#     if num == 0:
#         return 0
#     return 1+calculate_no_of_digit(num//10)
#
#
# num = 124353
# print(calculate_no_of_digit(num))


# # By converting it in string
# def calculate_digit(num):
#     num_in_string = str(num)
#     len_of_num = len(num_in_string)
#     return len_of_num
#
# print(calculate_digit(432))


# Using log
import math


def count_numbers(num):
    return math.floor(math.log10(num)+1)


num = 65432398
print(count_numbers(num))
