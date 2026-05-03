class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        max_frequency = 0
        char_counter = [0] * 26

        while right < len(s):
            char_counter[ord(s[right]) - ord('A')] +=1

            max_frequency = max(max_frequency, char_counter[ord(s[right]) - ord('A')])

            while right-left+1 > max_frequency + k:
                char_counter[ord(s[left]) - ord('A')]-=1
                left+=1
            
            right+=1
        
        return right - left