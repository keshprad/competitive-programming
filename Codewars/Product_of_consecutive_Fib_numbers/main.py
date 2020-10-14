# Problem: https://www.codewars.com/kata/5541f58a944b85ce6d00006a


def productFib(prod):
    prev, curr = 0, 1
    while prev*curr < prod:
        prev, curr = curr, prev + curr
    return [prev, curr, prev*curr == prod]
