# https://leetcode.com/problems/container-with-most-water/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        width = len(height) -1

        curr_area = min(height[left], height[right]) * width
        max_area = curr_area

        while left < right:
            curr_area = min(height[left], height[right]) * width

            if curr_area > max_area:
                max_area = curr_area

            if height[left] < height[right]:
                left += 1
            else: 
                right -= 1

            width -= 1

        return max_area