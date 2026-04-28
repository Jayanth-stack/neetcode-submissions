class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_array = [1] * n
        right_array = [1] * n

        prefix = 1
        postfix = 1

        for i in range(n):
            left_array[i] = prefix
            prefix *= nums[i]
        
        for i in range(n-1, -1, -1):
            right_array[i] = postfix
            postfix *= nums[i]
        
        return [l*r for l, r in zip(left_array, right_array)]