# Problem: https://www.hackerrank.com/challenges/sock-merchant/problem


def sockMerchant(ar):
    stock = {}
    for color in ar:
        if color not in stock:
            stock[color] = 0
        stock[color] += 1

    pairs = 0
    for num in stock.values():
        pairs += num//2
    return pairs


if __name__ == "__main__":
    n = int(input())
    ar = list(map(int, input().replace(",", " ").split()))
    print(sockMerchant(ar))
