# Problem: https://www.codewars.com/kata/545cedaa9943f7fe7b000048


def is_pangram(s):
    found = []
    for char in s:
        if char.isalpha() and char.lower() not in found:
            found.append(char.lower())
    return len(found) == 26
