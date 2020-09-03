# Problem: https://codeforces.com/problemset/problem/996/A

def main(n):
    bill_types = [100, 20, 10, 5, 1]
    bill_count = 0

    for bill in bill_types:
        bill_count += n // bill
        n %= bill
    return bill_count


if __name__ == "__main__":
    n = int(input())
    print(main(n))
