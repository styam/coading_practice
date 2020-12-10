"""
Calculate factorial of the number
"""

def factorial_num(num):
    return 1 if(num == 0 or num == 1) else num*factorial_num(num-1)


num = 5
print(factorial_num(num))