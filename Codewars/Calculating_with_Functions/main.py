# Problem: https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39


def zero(p=None):
    if p is None:
        return 0
    else:
        return handle_operator(op=p[0], num1=0, num2=p[1])


def one(p=None):
    if p is None:
        return 1
    else:
        return handle_operator(op=p[0], num1=1, num2=p[1])


def two(p=None):
    if p is None:
        return 2
    else:
        return handle_operator(op=p[0], num1=2, num2=p[1])


def three(p=None):
    if p is None:
        return 3
    else:
        return handle_operator(op=p[0], num1=3, num2=p[1])


def four(p=None):
    if p is None:
        return 4
    else:
        return handle_operator(op=p[0], num1=4, num2=p[1])


def five(p=None):
    if p is None:
        return 5
    else:
        return handle_operator(op=p[0], num1=5, num2=p[1])


def six(p=None):
    if p is None:
        return 6
    else:
        return handle_operator(op=p[0], num1=6, num2=p[1])


def seven(p=None):
    if p is None:
        return 7
    else:
        return handle_operator(op=p[0], num1=7, num2=p[1])


def eight(p=None):
    if p is None:
        return 8
    else:
        return handle_operator(op=p[0], num1=8, num2=p[1])


def nine(p=None):
    if p is None:
        return 9
    else:
        return handle_operator(op=p[0], num1=9, num2=p[1])


def plus(p):
    return ["+", p]


def minus(p):
    return ["-", p]


def times(p):
    return ["*", p]


def divided_by(p):
    return ["//", p]


def handle_operator(op, num1, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "//":
        return num1 // num2
