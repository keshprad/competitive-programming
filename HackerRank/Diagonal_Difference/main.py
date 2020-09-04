# Problem: https://www.hackerrank.com/challenges/diagonal-difference/problem


def diagonalDifference(arr):
    side = len(arr)
    left2right, right2left = 0, 0

    for i in range(len(arr)):
        left2right += arr[i][i]
        right2left += arr[i][-i - 1]
    return abs(left2right - right2left)


if __name__ == "__main__":
    n = int(input())
    arr = []
    for i in range(n):
        l = input().replace(",", " ").split()
        arr.append([int(num) for num in l])
    print(diagonalDifference(arr))
