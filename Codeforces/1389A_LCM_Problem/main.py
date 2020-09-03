# Problem: https://codeforces.com/problemset/problem/1389/A

def main(l, r):
    if l * 2 > r:
        return -1, -1
    else:
        return l, l * 2


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        values = input().split()
        l, r = int(values[0]), int(values[1])

        print(*main(l, r))
