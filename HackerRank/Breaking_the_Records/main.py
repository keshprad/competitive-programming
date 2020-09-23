# Problem: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem


def breakingRecords(scores):
    min_score, min_count, max_score, max_count = scores[0], 0, scores[0], 0

    for score in scores:
        if score < min_score:
            min_count += 1
            min_score = score
        elif score > max_score:
            max_count += 1
            max_score = score
    return max_count, min_count

if __name__ == "__main__":
    n = int(input())
    scores = list(map(int, input().rstrip().split()))
    
    print(*breakingRecords(scores))