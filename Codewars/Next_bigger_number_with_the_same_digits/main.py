# Problem: https://www.codewars.com/kata/55983863da40caa2c900004e/


def next_bigger(n):
    n = list(str(n))

    # Finds non-increasing suffix
    l = len(n) - 1
    while l > 0 and n[l - 1] >= n[l]:
        l -= 1

    # This means there are no lexicographically greater orderings
    if l == 0:
        return -1

    # Find RIGHTMOST successor to pivot
    pivot, r = l - 1, len(n) - 1
    while n[pivot] >= n[r]:
        r -= 1
    n[pivot], n[r] = n[r], n[pivot]

    # Reverse suffix
    n[l:] = n[:pivot: -1]
    return int("".join(n))
