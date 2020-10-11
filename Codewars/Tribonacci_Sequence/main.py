# Problem: https://www.codewars.com/kata/556deca17c58da83c00002db


def tribonacci(signature, n):
    index = 3
    if n <= 3:
        return signature[:n]
    while len(signature) < n:
        signature.append(sum(signature[index - 3:index]))
        index += 1
    return signature
