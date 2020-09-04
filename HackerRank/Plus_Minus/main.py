# Problem: https://www.hackerrank.com/challenges/plus-minus/problem


def plusMinus(arr):
    # [pos, neg, zeros]
    ratios = [0.0] * 3
    for num in arr:
        if num > 0:
            ratios[0] += 1
        elif num < 0:
            ratios[1] += 1
        else:
            ratios[2] += 1
    ratios = ['%.6f' % (count / len(arr)) for count in ratios]
    return '\n'.join(ratios)


if __name__ == "__main__":
    n = int(input())
    arr = input().replace(",", " ").split()
    arr = [int(num) for num in arr]
    print(plusMinus(arr))
