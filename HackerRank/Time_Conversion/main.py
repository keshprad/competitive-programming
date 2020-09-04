# Problem: https://www.hackerrank.com/challenges/time-conversion/problem


def timeConversion(s):
    AMPM = s[-2:]
    time = s[:-2].split(sep=":")
    if AMPM == "PM":
        if time[0] != "12":
            time[0] = str(int(time[0]) + 12)
            return ":".join(time)
    elif time[0] == "12":
        time[0] = "00"
        return ":".join(time)
    return s[:-2]


if __name__ == "__main__":
    # input form: "hh:mm:ssAM" or "hh:mm:ssPM"
    time = input()
    print(timeConversion(time))
