from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=defaultdict(int)
        for i in range(len(nums)):
            curr=target-nums[i]
            if curr in a:
                return [a[curr],i]
            
            a[nums[i]]=i