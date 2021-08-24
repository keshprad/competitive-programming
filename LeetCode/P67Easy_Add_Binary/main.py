# Problem: https://leetcode.com/problems/add-binary/


class Solution:
    # Iterative Solution
    def addBinary(self, a: str, b: str) -> str:
        bin_sum = ''
        a, b = map(list, (a, b))

        carry = 0
        while a or b:
            # Iterate through each index in reverse order
            num1 = int(a.pop()) if a else 0
            num2 = int(b.pop()) if b else 0

            # Calculate a carry and a val for the current index
            carry, val = divmod(num1 + num2 + carry, 2)
            bin_sum += str(val)

        # If a carry is leftover from the loop, add to bin_sum
        bin_sum += str(carry) if carry else ''

        # Reverse order since binary sum was calculated & stored in reverse order
        return bin_sum[::-1]

    # Recursive solution
    def addBinary2(self, a: str, b: str) -> str:
        # Base cases to return after one list is empty
        if not a: return b
        if not b: return a

        # Compare last element to determine recursive case
        if a[-1] == '0' and b[-1] == '0':
            # binary sum = '0' at last index; recursively call on all but last index.
            return self.addBinary2(a[:-1], b[:-1]) + '0'
        elif a[-1] == '1' and b[-1] == '1':
            # binary sum = '10' at last index; recursively call on all but last index.
            # In order to carry the '1', make another recursive call to add '1' to current result
            return self.addBinary2(self.addBinary2(a[:-1], b[:-1]), '1') + '0'
        else:
            # binary sum = '1' at last index; recursively call on all but last index.
            return self.addBinary2(a[:-1], b[:-1]) + '1'
