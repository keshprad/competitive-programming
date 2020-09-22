# Problem: https://www.hackerrank.com/challenges/lisa-workbook/problem


def workbook(n, k, arr):
    curr_page = 1
    special_count = 0

    for ch in arr:
        for problem in range(1, ch+1):
            special_count += curr_page == problem
            curr_page += problem % k == 0 or problem == ch
    return special_count


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(workbook(n, k, arr))
