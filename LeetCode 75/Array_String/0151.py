# https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = []
        words = []
        word = []

        for char in s:
            s_list.append(char)

        if s_list[0] == ' ':
            while s_list[0] == ' ':
                s_list.pop(0)

        if s_list[-1] == ' ':
            while s_list[-1] == ' ':
                s_list.pop(-1)


        for i in range(len(s_list)-1, -1, -1):
            if s_list[i] == ' ':
                if word == []:
                    continue

                words.append(word)
                words.append(' ')
                word = []

            else:
                word.insert(0, s_list[i])

        words.append(word)

        for i in range(len(words)):
            if i % 2 == 0:
                words[i] = "".join(words[i])

        return "".join(words)

# This solution goes through the array 3 times on every execution.
# The first time, it produces a list, wich is more efficient for insertions and removals
# The second time, it gathers the words
# The third time, it converts the words, wich are lists, into strings
# The solution has an O(n) complexity