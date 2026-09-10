# https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u',
                  'A', 'E', 'I', 'O', 'U']

        vowels_found = []

        s_list = []
        for i in range(len(s)):
            s_list.append(s[i])

        for i in range(len(s)-1, -1, -1):
            if s[i] in vowels:
                vowels_found.append(s[i])

        for i in range(len(s_list)):
            if s_list[i] in vowels:
                s_list[i] = vowels_found.pop(0)     

        return "".join(s_list)

# This solution goes through the array 3 times on every execution, and, 
# In two of them, compares every char to the 10 possible vowels.
# So, the complexity is O(n + 2n * 10) = O(21n) = O(n)
# Surely, there is a better version of the solution using the two pointers approach