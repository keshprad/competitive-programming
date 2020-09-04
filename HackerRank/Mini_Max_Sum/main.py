# Problem: https://www.hackerrank.com/challenges/mini-max-sum/problem


def miniMaxSum(arr):
    total = sum(arr)
    mini_sum = total - max(arr)
    max_sum = total - min(arr)
    return mini_sum, max_sum


if __name__ == "__main__":
    arr = list(map(int, input().rstrip().split()))

    print(*miniMaxSum(arr))
