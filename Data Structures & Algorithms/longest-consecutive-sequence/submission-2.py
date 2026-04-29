class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = -math.inf
        for num in num_set:
            if num-1 not in num_set:
                curr = 1
                while num+curr in num_set:
                    curr+=1
            
                longest = max(longest, curr)
    
        return longest if len(nums) > 0 else 0