# https://leetcode.com/problems/maximum-average-subarray-i/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        if k > len(nums):
            return

        left = 0
        right = k-1

        curr_sum = 0
        for i in range(k):
            curr_sum += nums[i]

        max_sum = curr_sum

        while right < len(nums)-1:
            curr_sum -= nums[left]
            left += 1
            right += 1
            curr_sum += nums[right]

            if curr_sum > max_sum:
                max_sum = curr_sum

            

        return float(max_sum / k)