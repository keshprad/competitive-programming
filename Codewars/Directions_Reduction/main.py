# Problem: https://www.codewars.com/kata/550f22f4d758534c1100025a


def dirReduc(arr):
    NS = ["NORTH", "SOUTH"]
    EW = ["EAST", "WEST"]

    i = 1
    while i < len(arr):
        if arr[i] != arr[i - 1]:
            if (arr[i] in NS and arr[i - 1] in NS) or (arr[i] in EW and arr[i - 1] in EW):
                arr = arr[:i - 1] + arr[i + 1:]
                i = 0
        i += 1
    return arr
