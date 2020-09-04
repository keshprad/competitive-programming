# Problem: https://www.hackerrank.com/challenges/a-very-big-sum/problem


def aVeryBigSum(ar):
    return sum(ar)


if __name__ == "__main__":
    n = int(input("Num elements: "))
    ar = input().replace(",", " ").split()
    ar = [int(num) for num in ar]

    print(aVeryBigSum(ar))
