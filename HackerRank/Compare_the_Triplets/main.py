# Problem: https://www.hackerrank.com/challenges/compare-the-triplets/problem


def compareTriplets(a, b):
    a_score, b_score = 0, 0

    for i in range(len(a)):
        if a[i] > b[i]:
            a_score += 1
        elif b[i] > a[i]:
            b_score += 1
    return [a_score, b_score]


if __name__ == "__main__":
    # A's scores
    a = input().replace(",", " ").split()
    a = [int(item) for item in a]

    # B's scores
    b = input().replace(",", " ").split()
    b = [int(item) for item in b]
    print(*compareTriplets(a, b))
