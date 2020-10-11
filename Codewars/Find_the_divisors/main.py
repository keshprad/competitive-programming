# Problem: https://www.codewars.com/kata/544aed4c4a30184e960010f4


def divisors(integer):
    res = []
    for i in range(2, integer):
        if integer % i == 0:
            res.append(i)
    if len(res) == 0:
        return "{num} is prime".format(num=integer)
    return res
