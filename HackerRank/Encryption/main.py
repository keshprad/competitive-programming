import math
# Problem: https://www.hackerrank.com/challenges/encryption/problem


def encryption(s):
    root = math.sqrt(len(s))
    rows, cols = math.floor(root), math.ceil(root)

    if rows * cols < len(s):
        rows += 1

    result=""
    for c in range(cols):
        index = c
        while index < len(s):
            result += s[index]
            index += cols
        result += " "
    return result


if __name__ == "__main__":
    s = input()
    print(encryption(s))
