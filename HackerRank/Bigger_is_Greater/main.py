# Problem: https://www.hackerrank.com/challenges/bigger-is-greater/problem


def biggerIsGreater(w):
    w = list(w)

    # Find non-increasing suffix
    l = len(w) - 1
    while l > 0 and w[l - 1] >= w[l]:
        l -= 1

    # This means there are no lexicographically greater orderings
    if l == 0:
        return "no answer"

    # Find RIGHTMOST successor to pivot
    pivot, r = l - 1, len(w) - 1
    while w[pivot] >= w[r]:
        r -= 1
    w[pivot], w[r] = w[r], w[pivot]

    # Reverse suffix
    w[l:] = w[:pivot: -1]
    return "".join(w)


if __name__ == '__main__':
    n = int(input())
    res = []
    for i in range(n):
        word = input()
        res.append(biggerIsGreater(word))
    print(*res, sep="\n")
