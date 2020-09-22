# Problem: https://www.hackerrank.com/challenges/halloween-sale/problem


def howManyGames(p, d, m, s):
    num_games = 0

    while s >= p:
        s -= p
        num_games += 1
        if p-d <= m:
            p = m
        else:
            p -= d
    return num_games

if __name__ == "__main__":
    p, d, m, s = list(map(int, input().split()))
    print(howManyGames(p, d, m, s))