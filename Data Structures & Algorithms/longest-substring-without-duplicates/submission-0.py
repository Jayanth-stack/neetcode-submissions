class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_pointer = 0
        max_len = 0

        hashset = set()

        for right_pointer in range(len(s)):

            while s[right_pointer] in hashset:
                hashset.remove(s[left_pointer])
                left_pointer+=1
            

            hashset.add(s[right_pointer])

            max_len = max(max_len, right_pointer - left_pointer + 1)
        
        return max_len


        

