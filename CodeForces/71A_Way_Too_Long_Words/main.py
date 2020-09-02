# Problem: https://codeforces.com/problemset/problem/71/A

def main(words):
    for each in enumerate(words):
        index = each[0]
        word = each[1]

        if len(word) > 10:
            words[index] = word[0] + str(len(word) - 2) + word[-1]
    return words


if __name__ == "__main__":
    n = int(input())
    words = [input() for i in range(n)]

    abbreviated = main(words)
    print(*abbreviated, sep="\n")