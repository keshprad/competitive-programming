import math


# Problem: https://codeforces.com/problemset/problem/1389/A

def main(l, r):
    # for loops limit values of x and y to be in required range
    for x in range(l, r + 1):
        for y in range(x + 1, r + 1):

            # Finding LCM
            gcd = math.gcd(x, y)
            lcm = x * y // gcd

            # Check if LCM is in required range
            if l <= lcm <= r:
                return x, y
    return -1, -1


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        values = input().split()
        l, r = int(values[0]), int(values[1])

        print(*main(l, r))