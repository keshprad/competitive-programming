# Problem: https://codeforces.com/problemset/problem/427/A

def main(events):
    curr_officers, unsolved_crimes = 0, 0

    for event in events:
        if event > 0:
            curr_officers += event
        else:
            if curr_officers >= 1:
                curr_officers -= 1
            else:
                unsolved_crimes += 1
    return unsolved_crimes


if __name__ == "__main__":
    n = int(input())
    events = input().split()
    events = [int(event) for event in events]

    print(main(events))
