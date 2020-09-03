# Problem: https://codeforces.com/problemset/problem/705/A

def main(n):
    quote = []
    for i in range(n):
        if i % 2 == 0:
            quote.append("I hate")
        else:
            quote.append("I love")
    return " that ".join(quote) + " it"


if __name__ == "__main__":
    n = int(input())
    print(main(n))
