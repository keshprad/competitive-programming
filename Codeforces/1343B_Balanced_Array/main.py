# Problem: https://codeforces.com/problemset/problem/1343/B


def main(n):
    if n // 2 % 2 == 1:
        return "NO"
    else:
        valid = "YES\n"
        l_half, r_half = [], []
        l_sum, r_sum = 0, 0

        for i in range(2, n+1, 2):
            l_half.append(str(i))
            l_sum += i
        for j in range(1, n-2, 2):
            r_half.append(str(j))
            r_sum += j
        r_half.append(str(l_sum - r_sum))

        return valid + " ".join(l_half + r_half)

if __name__ == "__main__":
    # Take input
    t = int(input())
    cases = []
    for i in range(t):
        cases.append(int(input()))

    # Run main
    for case in cases:
        print(main(case))
