# https://leetcode.com/problems/max-consecutive-ones-iii/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        flipped = 0
        right = 0
        left = 0
        curr_ones = 0
        max_ones = 0

        while right < len(nums):
            if nums[right] == 0:
                if flipped < k:
                    flipped += 1
                    curr_ones += 1
                    right += 1

                else:
                    while nums[left] != 0:
                        left += 1
                        curr_ones -= 1

                    left += 1
                    flipped -= 1
                    curr_ones -= 1
            
            else:
                curr_ones += 1
                right += 1

            if curr_ones > max_ones:
                max_ones = curr_ones

        return max_ones