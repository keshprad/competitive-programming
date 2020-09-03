# Problem: https://codeforces.com/problemset/problem/977/A

def main(n, k):
    for i in range(k):
        if n % 10 == 0:
            n //= 10
        else:
            n -= 1
    return n

if __name__ == "__main__":
    input = input().split()
    n, k = int(input[0]), int(input[1])

    print(main(n, k))