# Problem: https://www.hackerrank.com/challenges/the-time-in-words/problem


def timeInWords(h, m):
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight", "twenty nine", "half"]
    if m == 0:
        return numbers[h-1] + " o' clock"
    else:
        # Find a, c, and d
        if m <= 30:
            a = numbers[m-1]
            c = "past"
            d = numbers[h-1]
        else:
            a = numbers[60-m-1]
            c = "to"
            d = numbers[h]

        # Find b
        b = "minute"
        if m == 1:
            return " ".join((a, b, c, d))
        elif m != 15 and m != 30 and m != 45:
            return " ".join((a, b + "s", c, d))
        else:
            return " ".join((a, c, d))




if __name__ == "__main__":
    h = int(input().strip())
    m = int(input().strip())
    print(timeInWords(h, m))
