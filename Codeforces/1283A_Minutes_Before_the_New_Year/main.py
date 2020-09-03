# Problem: https://codeforces.com/problemset/problem/1283/A

def main(hr, min):
    total_min = 24 * 60
    curr_time = (hr * 60) + min

    return total_min - curr_time

if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        values = input().split()
        curr_hour, curr_min = int(values[0]), int(values[1])
        print(main(curr_hour, curr_min))