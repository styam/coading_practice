def is_prime(num):
    for i in range(2, num):
        if num % i ==0:
            return False
        
        return True


def prime_generate(n):
    num = 2
    while n:
        if is_prime(num):
            yield num
            n -= 1
        num+= 1
    return


it = prime_generate(10)
for e in it:
    print(e, end= ' ')
