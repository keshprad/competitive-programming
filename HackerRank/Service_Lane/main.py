# Problem:


def serviceLane(width, cases):
    result = []
    for case in cases:
        result.append(min(width[case[0]:case[1] + 1]))
    return result


if __name__ == "__main__":
    nk = list(map(int, input().replace(",", " ").split()))
    width = list(map(int, input().replace(",", " ").split()))
    cases = []
    for i in range(nk[1]):
        cases.append(list(map(int, input().replace(",", " ").split())))
    print(*serviceLane(width, cases), sep="\n")
