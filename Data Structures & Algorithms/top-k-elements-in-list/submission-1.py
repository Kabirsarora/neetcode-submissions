from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        a=defaultdict(int)
        for num in nums:
            a[num]+=1
        
        heap=[]
        for key in a.keys():
            heapq.heappush(heap,(-a[key],key))
        
        for i in range(k):
            amount,number=heapq.heappop(heap)
            ans.append(number)
        
        return ans