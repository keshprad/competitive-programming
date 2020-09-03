# Problem: https://codeforces.com/problemset/problem/486/A

def main(n):
    if n % 2 == 0:
        return n // 2
    else:
        return -(n // 2 + 1)


if __name__ == "__main__":
    n = int(input())
    print(main(n))
