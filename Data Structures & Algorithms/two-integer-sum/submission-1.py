class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        two_sum = {}

        for i, value in enumerate(nums):
            if target - value in two_sum:
                return [two_sum[target-value], i]
            
            else:
                two_sum[value] = i
        
        return -1