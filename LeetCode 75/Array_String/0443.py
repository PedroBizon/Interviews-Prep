# https://leetcode.com/problems/string-compression/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def compress(self, chars: List[str]) -> int:
        # Edge case:
        if len(chars) == 1:
            return 1
        
        chars2 = []

        i = 0
        while i < len(chars):
            curr_char = chars[i]
            counter = 0

            # Counting consecutive duplicates
            while i < len(chars) and chars[i] == curr_char:
                counter += 1
                i += 1

            # Putting the result into the chars2 list
            chars2.append(curr_char)

            # Putting the counter into the chars2 list
            if counter == 1:
                continue
            
            counter_list = []
            while counter > 0:
                counter_list.insert(0, counter % 10)
                counter = counter // 10
            
            for j in range(len(counter_list)):
                chars2.append(counter_list[j]) 
                
        print(chars2)
        for j in range(len(chars2)):
            chars[j] = str(chars2[j])


        return len(chars2)