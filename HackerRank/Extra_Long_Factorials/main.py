# Problem: https://www.hackerrank.com/challenges/extra-long-factorials/problem


def extraLongFactorials(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


if __name__ == "__main__":
    n = int(input().strip())
    print(extraLongFactorials(n))
