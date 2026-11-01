class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)==0:
            return 0
        ans=1
        curr=1
        for i in range(1,len(nums)):
            if nums[i-1]+1==nums[i]:
                curr+=1
            elif nums[i-1]==nums[i]:
                continue
            else:
                ans=max(ans,curr)
                curr=1
        ans=max(ans,curr)
        
        return ans