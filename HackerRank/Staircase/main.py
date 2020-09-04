# Problem: https://www.hackerrank.com/challenges/staircase/problem


def staircase(n):
    result = []
    for i in range(1, n+1):
        result.append(" "*(n-i) + "#"*i)
    return '\n'.join(result)


if __name__ == '__main__':
    n = int(input())
    print(staircase(n))
