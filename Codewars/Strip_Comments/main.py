# Problem: https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python


def solution(string, markers):
    string = string.split(sep="\n")
    for i in range(len(string)):
        curr = string[i]
        for j in range(len(curr)):
            char = curr[j]
            if char in markers:
                string[i] = curr[:j].rstrip()
                break
    return "\n".join(string)
