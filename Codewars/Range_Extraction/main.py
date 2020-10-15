# Problem: https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/


def solution(args):
    args = sorted(args)

    res, start, i = [], 0, 1
    while i <= len(args):
        if i == len(args) or args[i - 1] + 1 != args[i]:
            if i - start > 2:
                res.append(str(args[start]) + "-" + str(args[i - 1]))
            else:
                for s in args[start:i]:
                    res.append(str(s))
            start = i
        i += 1
    return ",".join(res)
