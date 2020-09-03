# Problem: https://leetcode.com/problems/two-sum/


def main(nums, target):
    diff = {}

    for i in range(len(nums)):
        item = nums[i]

        if target - item not in diff:
            diff[item] = i
        else:
            return [diff[target - item], i]


if __name__ == '__main__':
    nums = input("array of integers: ").replace(",", " ").split()
    nums = [int(num) for num in nums]
    target = int(input("target integer: "))

    print(main(nums, target))
