class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        num_set = len(set(nums))

        if num_set != n:
            return True
        else:
            return False
