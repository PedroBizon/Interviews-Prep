# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']

        if len(s) < k:
            return

        curr_total = 0

        for i in range(k):
            if s[i] in vowels:
                curr_total += 1

        highest_total = curr_total

        right = k-1
        left = 0

        while right < len(s) - 1:
            if s[left] in vowels:
                curr_total -= 1

            left += 1
            right += 1

            if s[right] in vowels:
                curr_total += 1

            if curr_total > highest_total:
                highest_total = curr_total
            
        return highest_total