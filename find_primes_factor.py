def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def primes():
    res = []

    for i in range(2, 100):
        if is_prime(i):
            res.append(i)
    return res


def solve(n):
    if is_prime(n):
        return n

    res = []

    while n > 1:
        for i in primes():
            if n % i == 0:
                res.append(i)
                n //= i
                print(n)

    return res



print(solve(630))