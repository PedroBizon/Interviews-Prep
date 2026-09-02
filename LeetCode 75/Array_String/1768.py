# https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        j = 0
        l1 = len(word1)
        l2 = len(word2)

        ans = []

        while i < l1 and j < l2:
            ans.append(word1[i])
            ans.append(word2[j])

            i += 1
            j += 1

        ans.append(word1[i:])
        ans.append(word2[j:])

        return "".join(ans)