# https://leetcode.com/problems/move-zeroes/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        i = 0
        zeroes = 0
        while i < len(nums) - zeroes:
            if nums[i] == 0:
                nums.pop(i)
                nums.append(0)
                zeroes += 1

            else:
                i += 1

        