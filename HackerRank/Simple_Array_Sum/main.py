# Problem: https://www.hackerrank.com/challenges/simple-array-sum/problem


def simpleArraySum(ar):
    return sum(ar)


if __name__ == "__main__":
    ar = input("Array of Integers: ").replace(",", " ").split()
    ar = [int(item) for item in ar]
    print(simpleArraySum(ar))
