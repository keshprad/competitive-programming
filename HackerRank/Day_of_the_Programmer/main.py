# Problem: https://www.hackerrank.com/challenges/day-of-the-programmer/problem


def dayOfProgrammer(year):
    if (year == 1918):
        return '26.09.1918'
    elif ((year <= 1917) & (year%4 == 0)) or ((year > 1918) & (year%400 == 0 or ((year%4 == 0) & (year%100 != 0)))):
        return '12.09.{y:}'.format(y = year)
    else:
        return '13.09.{y:}'.format(y = year)


if __name__ == "__main__":
    year = int(input())
    print(dayOfProgrammer(year))