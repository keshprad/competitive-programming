# Problem: https://codeforces.com/problemset/problem/59/A

def main(word):
    upper_count = 0

    # Find num characters that are lower/upper case
    for letter in word:
        if letter.isupper():
            upper_count += 1
    lower_count = len(word) - upper_count

    # Determine which case to use
    if upper_count > lower_count:
        return word.upper()
    return word.lower()


if __name__ == "__main__":
    word = input()
    print(main(word))
