from math import sqrt


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        f1, f2 = [], []
        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                f1.append(i)
                f2.append(n // i)
            if len(f1) >= k:
                break

        # If the n is a square number, remove the duplicate factor
        if f1[-1] == f2[-1]:
            f2 = f2[:-1]
        # Combine the lists of factors
        f1 = f1 + f2[::-1]

        # Return the kth factor or -1
        if len(f1) >= k:
            return f1[k-1]
        else:
            return -1
