# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        most_candies = 0

        # 1. Find out how many candies the kid with the most has
        for i in range(len(candies)):
            if candies[i] > most_candies:
                most_candies = candies[i]

        # 2. Fill up the result list
        for i in range(len(candies)):
            if candies[i] + extraCandies >= most_candies:
                result.append(True)
            else:
                result.append(False)

        return result

# This solution goes through the array 2 times on every execution
# So, the complexity is O(2n), wich is O(n)