class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for ele, value in enumerate(nums):
            freq[value]+=1
        heap = []

        for key, value in freq.items():
            heapq.heappush(heap, (-value, key))
        
        result = []
        while k>0:
            value, key = heapq.heappop(heap)
            k-=1
            result.append(key)

        return result
