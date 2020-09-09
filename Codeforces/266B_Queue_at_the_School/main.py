# Problem: https://codeforces.com/problemset/problem/266/B


def main(queue, t):
    for j in range(t):
        # Find indices to switch
        to_switch = []
        curr_ind = queue.find("BG", 0)
        while curr_ind != -1:
            to_switch.append(curr_ind)
            curr_ind = queue.find("BG", curr_ind+1, len(queue))

        # switch B and G
        for i in to_switch:
            queue = queue[:i] + "GB" + queue[i+2:]
    return queue


if __name__ == '__main__':
    nt = list(map(int, input().split()))
    n, t = nt[0], nt[1]
    queue = input().strip()
    print(main(queue, t))

