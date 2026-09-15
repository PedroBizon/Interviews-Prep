# https://leetcode.com/problems/increasing-triplet-subsequence/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        smallest = nums[0]

        # Finding the middle number
        middle = 0
        j = 0
        for i in range(1, len(nums)):
            if nums[i] <= smallest:
                smallest = nums[i]

            else:
                middle = nums[i]
                j = i
                break

        # Failed to get middle number, meaning the first number is the biggest
        if j == 0:
            return False
        
        for i in range(j+1, len(nums)):
            if nums[i] <= smallest:
                smallest = nums[i]

            elif nums[i] <= middle:
                middle = nums[i]

            else:
                print((smallest, middle))
                return True

        return False