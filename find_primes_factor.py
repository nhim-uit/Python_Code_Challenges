# Linked Learning - Python Code Challenges
# 14 Jul, 2025
# Find prime factors
# Created by me (Alex M)

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
                # print(n)

    return res


# solution solve2 by Barron Stone
def solve2(n):
    factors = list()
    divisor = 2
    while (divisor <= n):
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        else:
            divisor += 1
        # print(divisor)
    return factors


# print(solve2(630))
# print(solve2(13))
print(solve2(5040))
print(solve(5040))
