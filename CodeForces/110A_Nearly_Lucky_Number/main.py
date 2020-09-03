# Problem: https://codeforces.com/problemset/problem/110/A

def main(n):
    n, lucky_digits = str(n), [4, 7]
    lucky_count = 0

    for digit in n:
        digit = int(digit)
        if digit in lucky_digits:
            lucky_count += 1

    if lucky_count in lucky_digits:
        return "YES"
    else:
        return "NO"

if __name__ == "__main__":
    n = int(input())
    print(main(n))