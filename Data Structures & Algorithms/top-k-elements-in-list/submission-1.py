class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_elements = defaultdict(int)
        heap =[]

        for ele, value in enumerate(nums):
            freq_elements[value]+=1
        
        for key, value in freq_elements.items():
            heapq.heappush(heap, (-value, key))
        
        result = []

        while k>0:
            value, key = heapq.heappop(heap)
            k-=1
            result.append(key)
        
        return result


        
        
