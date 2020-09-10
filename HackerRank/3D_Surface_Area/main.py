# Problem: https://www.hackerrank.com/challenges/3d-surface-area/problem


def surfaceArea(A):
    # Create new array with padding of 0s
    pad = [(0,) * (len(A[0]) + 2)] + [(0,) + tuple(each) + (0,) for each in A] + [(0,) * (len(A[0]) + 2)]

    # Area of Top and Bottom
    s_area = len(A) * len(A[0]) * 2

    # Area for sides
    for row in range(1, len(pad)):
        for col in range(1, len(pad[0])):
            # Left and Right sides
            s_area += abs(pad[row][col] - pad[row][col - 1])
            # Front and Back sides
            s_area += abs(pad[row][col] - pad[row - 1][col])
    return s_area


if __name__ == '__main__':
    hw = list(map(int, input().split()))

    A = [list(map(int, input().split())) for i in range(hw[0])]
    print(surfaceArea(A))
