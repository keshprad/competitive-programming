# Problem: https://www.codewars.com/kata/57eb8fcdf670e99d9b000272


def high(x):
    base = ord("a") - 1
    x = x.split()
    scores = []

    for word in x:
        scores.append(sum(ord(c) - base for c in word))
    max_score_index = scores.index(max(scores))
    return x[max_score_index]
