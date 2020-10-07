# Problem: https://www.hackerrank.com/challenges/the-birthday-bar/problem

def birthday(s, d, m):
    combos = 0;
    for i in range(len(s)-m+1):
        combos += sum(s[i:i+m]) == d
    return combos

if __name__ == "__main__":
    n = int(input().strip())
    s = list(map(int, input().rstrip().split()))
    dm = input().strip().split()
    d, 6
1 1 1 1 1 1
3 2m = int(dm[0]), int(dm[1])
    print(birthday(s, d, m))