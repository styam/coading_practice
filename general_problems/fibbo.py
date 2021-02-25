# ==================Using single for loop==================
fibonacci_numbers = [0, 1]
for i in range(2,10):
    fibonacci_numbers.append(fibonacci_numbers[i-1]+fibonacci_numbers[i-2])

print(fibonacci_numbers)

#========================Use recursion )============================= :

def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(9))

# ========================Using DP==================

lst = [0, 1]


def fibonacci(n):
    if n <= 0:
        print("Incorrect input")

    # Check is n is less
    # than len(FibArray)
    elif n <= len(lst):
        return lst[n - 1]
    else:
        temp_fib = fibonacci(n - 1) + fibonacci(n - 2)
    lst.append(temp_fib)
    return temp_fib


print(fibonacci(9))

