# Problem: https://codeforces.com/problemset/problem/510/A

def main(rows, cols):
    if rows == 0 or cols == 0:
        return ""

    snake = []
    for i in range(rows):
        if i % 2 == 0:
            snake.append("#" * cols)
        elif i % 4 == 1:
            snake.append("." * (cols - 1) + "#")
        elif i % 4 == 3:
            snake.append("#" + "." * (cols - 1))
    return "\n".join(snake)


if __name__ == "__main__":
    vals = input().split()
    rows, cols = int(vals[0]), int(vals[1])
    print(main(rows, cols))
