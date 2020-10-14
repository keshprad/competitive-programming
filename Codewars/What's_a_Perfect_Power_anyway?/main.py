import math

# Problem: https://www.codewars.com/kata/54d4c8b08776e4ad92000835/


def isPP(n):
    for base in range(2, int(math.sqrt(n)) + 1):
        power = int(round(math.log(n, base)))
        if base ** power == n:
            return [base, power]
    return None
