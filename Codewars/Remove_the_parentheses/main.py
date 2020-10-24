# Problem: https://www.codewars.com/kata/5f7c38eb54307c002a2b8cc8/


def remove_parentheses(s):
    p, res = 0, ""
    for char in s:
        p += char == "("
        if p == 0:
            res += char
        p -= char == ")"
    return res