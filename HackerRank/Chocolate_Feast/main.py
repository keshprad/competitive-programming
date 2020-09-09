# Problem: https://www.hackerrank.com/challenges/chocolate-feast/problem


def chocolateFeast(n, c, m):
    bars = n // c
    bank = bars

    while bank >= m:
        new_bars = bank // m
        bars += new_bars
        bank += new_bars - (new_bars * m)
    return bars


if __name__ == "__main__":
    vals = list(map(int, input().split()))
    n, c, m = vals[0], vals[1], vals[2]
    print(chocolateFeast(n, c, m))
