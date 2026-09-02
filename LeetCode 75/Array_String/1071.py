# https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        i = 0

        if len(str1) > len(str2):
            shorter = str2
            longer = str1
        else:
            shorter = str1
            longer = str2

        while i < len(shorter):
            candidate = shorter[:i]

            if self.dividesBoth(candidate, shorter, longer):
                ans = candidate

        return ans

    def dividesBoth(self, candidate, shorter, longer):
        if self.divides(candidate, shorter) and self.divides(candidate, longer):
            return True

    def divides(self, candidate, word):
        original_candidate = candidate

        while len(candidate) <= len(word):
            if candidate == word:
                return True
            else:
                candidate += original_candidate

        return False

        

        
            