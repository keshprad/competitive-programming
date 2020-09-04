# Problem: https://www.hackerrank.com/challenges/bon-appetit/problem


def bonAppetit(bill, k, b):
    expected = (sum(bill) - bill[k]) / 2
    if expected == b:
        return "Bon Appetit"
    return int(b - expected)


if __name__ == "__main__":
    nk = input().rstrip().split()
    k = int(nk[1])
    bill = list(map(int, input().replace(",", " ").split()))
    b = int(input())

    print(bonAppetit(bill, k, b))
