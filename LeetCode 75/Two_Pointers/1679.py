# https://leetcode.com/problems/max-number-of-k-sum-pairs/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        appearences = {}
        ans = 0

        for i in range(len(nums)):
            if nums[i] < k:

                if nums[i] in appearences.keys():
                    ans += 1
                    if appearences[nums[i]] > 1:
                        appearences[nums[i]] -= 1
                    else:
                        appearences.pop(nums[i])

                else:
                    if (k - nums[i]) in appearences.keys():
                        appearences[k - nums[i]] += 1
                    else:
                        appearences[k - nums[i]] = 1

        return ans