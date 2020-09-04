# Problem: https://www.hackerrank.com/challenges/birthday-cake-candles/problem


def birthdayCakeCandles(ar):
    height = max(ar)
    tall_candles = ar.count(height)
    return tall_candles


if __name__ == "__main__":
    ar = list(map(int, input().rstrip().split()))
    print(birthdayCakeCandles(ar))
