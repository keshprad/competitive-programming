package LeetCode.P371Medium_Sum_of_Two_Integers;
// Problem: https://leetcode.com/problems/sum-of-two-integers/

class Solution {
    public int getSum(int a, int b) {
        int carry = 1;
        while (carry != 0) {
            carry = (a & b) << 1;
            a = a ^ b;
            b = carry;
        }
        return a;
    }
}