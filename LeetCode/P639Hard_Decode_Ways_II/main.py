# Problem: https://leetcode.com/problems/decode-ways-ii/


class Solution:
    # 2nd solution with O(1) space and O(n) time:
    def numDecodings(self, s: str) -> int:
        # Exit early if falsy
        if not s:
            return 0

        # Initialize dynamic programming array
        dp_i2 = 1
        dp_i1 = int(s[0] != '0') * (9 if s[0] == '*' else 1)
        dp_i = 0

        for i in range(1, len(s)):
            # Either a 1 digit or 2 digit string -> int is possible
            one_digit, two_digit = s[i], s[i - 1:i + 1]
            # Combo to multiply against num decodings at 1 index behind current index
            one_prev_combos = 0
            # Combo to multiply against num decodings at 2 indices behind current index
            two_prev_combos = 0

            # '*' not in curr step. Treat normally
            if '*' not in two_digit:
                one_digit, two_digit = int(one_digit), int(two_digit)
                # If digit is between 1-9, combo for previous index is 1
                one_prev_combos = 1 if 1 <= one_digit <= 9 else 0
                # If 2 digits is between 10-26, combo for 2 indices behind is 1
                two_prev_combos = 1 if 10 <= two_digit <= 26 else 0

            # '*' for both digits ('**')
            elif two_digit == '**':
                # 9 combos (1-9) for '*' at s[i] if we treat '**' as 1 digit numbers.
                one_prev_combos = 9
                # 15 possible combos if we treat '**' as a single 2 digit number: '**' is [11, 19] or [21, 26]
                two_prev_combos = 15

            # '*' is in tens place
            elif two_digit[0] == '*':
                one_digit = int(one_digit)
                # If digit is not 0 combo is 1 and one prev index is used.
                # If digit is 0, combo is zero. Only 2 digit nums possible, will use two_prev_combos only.
                one_prev_combos = int(one_digit != 0)
                # 2 combos (1 or 2) if one's place is between 0-6. 1 combo (only 1) if one's place is between 7-9
                two_prev_combos = 2 if 0 <= one_digit <= 6 else 1

            # '*' is in one's place
            elif one_digit == '*':
                tens_place = int(two_digit[0])
                # 9 combos possible: 1-9
                one_prev_combos = 9
                # 9 combos possible (11-19) if ten's place is 1. 6 combos possible (21-26) if ten's place is 2
                two_prev_combos = 9 if tens_place == 1 else 6 if tens_place == 2 else 0

            dp_i += dp_i1 * one_prev_combos
            dp_i += dp_i2 * two_prev_combos
            dp_i2, dp_i1, dp_i = dp_i1, dp_i % int(1e9 + 7), 0
        return dp_i1

    # Solution with O(n) space and time:
    def numDecodings1(self, s: str) -> int:
        # Exit early if falsy
        if not s:
            return 0

        # Initialize dynamic programming array
        dp = [0] * len(s)
        dp[0] = int(s[0] != '0') * (9 if s[0] == '*' else 1)

        for i in range(1, len(s)):
            # Either a 1 digit or 2 digit string -> int is possible
            one_digit, two_digit = s[i], s[i - 1:i + 1]
            # Combo to multiply against num decodings at 1 index behind current index
            one_prev_combos = 0
            # Combo to multiply against num decodings at 2 indices behind current index
            two_prev_combos = 0

            # '*' not in curr step. Treat normally
            if '*' not in two_digit:
                one_digit, two_digit = int(one_digit), int(two_digit)
                # If digit is between 1-9, combo for previous index is 1
                one_prev_combos = 1 if 1 <= one_digit <= 9 else 0
                # If 2 digits is between 10-26, combo for 2 indices behind is 1
                two_prev_combos = 1 if 10 <= two_digit <= 26 else 0

            # '*' for both digits ('**')
            elif two_digit == '**':
                # 9 combos (1-9) for '*' at s[i] if we treat '**' as 1 digit numbers.
                one_prev_combos = 9
                # 15 possible combos if we treat '**' as a single 2 digit number: '**' is [11, 19] or [21, 26]
                two_prev_combos = 15

            # '*' is in tens place
            elif two_digit[0] == '*':
                one_digit = int(one_digit)
                # If digit is not 0 combo is 1 and one prev index is used.
                # If digit is 0, combo is zero. Only 2 digit nums possible, will use two_prev_combos only.
                one_prev_combos = int(one_digit != 0)
                # 2 combos (1 or 2) if one's place is between 0-6. 1 combo (only 1) if one's place is between 7-9
                two_prev_combos = 2 if 0 <= one_digit <= 6 else 1

            # '*' is in one's place
            elif one_digit == '*':
                tens_place = int(two_digit[0])
                # 9 combos possible: 1-9
                one_prev_combos = 9
                # 9 combos possible (11-19) if ten's place is 1. 6 combos possible (21-26) if ten's place is 2
                two_prev_combos = 9 if tens_place == 1 else 6 if tens_place == 2 else 0

            dp[i] += dp[i - 1] * one_prev_combos
            dp[i] += (dp[i - 2] if i >= 2 else 1) * two_prev_combos
            dp[i] %= int(1e9 + 7)

        return dp[-1]


sol = Solution()
print(sol.numDecodings("*"))
print(sol.numDecodings("***"))
print(sol.numDecodings("1*"))
print(sol.numDecodings("2*"))
print(sol.numDecodings("*1"))
print(sol.numDecodings("*7"))
print(sol.numDecodings("*219*21*57"))
print(sol.numDecodings("*1*1*0"))
print(sol.numDecodings("1*6*7*1*9*6*2*9*2*3*3*6*3*2*2"))
print(
    sol.numDecodings(
        "1*6*7*1*9*6*2*9*2*3*3*6*3*2*2*4*7*2*9*6*0*6*4*4*1*6*9*0*5*9*2*5*7*7*0*6*9*7*1*5*5*9*3*0*4*9*2*6*2*5*7*6*1*9*4*5*8*4*7*4*2*7*1*2*1*9*1*3*0*6*"
    ))
