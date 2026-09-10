# https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        prefix = []
        postfix = []

        prefix.append(1)
        postfix.append(1)

        for i in range(1, len(nums)):
            prefix.append(nums[i-1] * prefix[-1]) 

        for i in range(len(nums)-2, 0, -1):
            postfix.insert(0, nums[i+1] * postfix[0])

        for i in range(len(nums)):
            ans.append(prefix[i] * postfix[i])

        return ans

# This solution goes through the array 3 times on every execution. 
# In two of them, it builds the prefix and postfix to every item in nums
# So, the complexity is O(3n) = O(n)
# Surely, it's possible to use only one loop to build both the prefix and postfix lists