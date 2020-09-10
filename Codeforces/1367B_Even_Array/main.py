# Problem: https://codeforces.com/problemset/problem/1367/B


def main(ar):
    evens, mismatches = 0, 0
    for i in range(len(ar)):
        num = ar[i]
        if num % 2 == 0:
            evens += 1
        if i % 2 != num % 2:
            mismatches += 1
    odds = len(ar) - evens

    if len(ar) % 2 != evens - odds:
        return -1
    else:
        return mismatches // 2


if __name__ == '__main__':
    n = int(input())
    results = []
    for i in range(n):
        l = int(input())
        case = list(map(int, input().replace(",", " ").split()))
        results.append(main(case))
    print(*results, sep="\n")
