# Problem: https://codeforces.com/problemset/problem/1325/B


def main(a):
    return len(set(a))


if __name__ == "__main__":
    t = int(input())
    cases = []
    for i in range(t):
        n = int(input())
        cases.append(list(map(int, input().replace(",", " ").split())))
    for case in cases:
        print(main(case))
