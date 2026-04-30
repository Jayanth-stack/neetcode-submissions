class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        n = len(nums)


        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left_ptr = i+1
            right_ptr = n-1

            while left_ptr < right_ptr:
                current_sum = nums[i] + nums[left_ptr] + nums[right_ptr]

                if current_sum == 0:
                    triplets.append([nums[i], nums[left_ptr], nums[right_ptr]])
            
                    while left_ptr < right_ptr and nums[left_ptr] == nums[left_ptr+1]:
                        left_ptr +=1
                
                    while left_ptr < right_ptr and nums[right_ptr]== nums[right_ptr -1]:
                        right_ptr -=1
                
                    left_ptr+=1
                    right_ptr-=1


                elif current_sum < 0:
                    left_ptr+=1
                else:
                    right_ptr-=1
        
        return triplets
    