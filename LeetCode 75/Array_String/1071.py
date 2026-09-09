# https://leetcode.com/problems/greatest-common-divisor-of-strings/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            longer = str1
            shorter = str2
        else:
            longer = str1
            shorter = str2

        candidate = []

        for i in range(len(shorter)):
            candidate.append(shorter[i])

             
        if(self.divides(candidate, shorter) and self.divides(candidate, longer)):
                gcd = "".join(candidate)
                return gcd

        for i in range(len(shorter)-1):
            candidate.pop(-1)

            if(self.divides(candidate, shorter) and self.divides(candidate, longer)):
                gcd = "".join(candidate)

                return gcd

        return ""
    


    def divides(self, candidate:list, word:str):
        if (len(word) % len(candidate) != 0):
            return False
        
        c = []

        for i in range(len(word)//len(candidate)):
            for j in range(len(candidate)):
                c.append(candidate[j])

        c_str = "".join(c)

        if (c_str == word):
            return True

        return False             
            