class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        mult=1
        zeros=0
        for i in range(len(nums)):
            if nums[i]==0:
                zeros+=1
                index=i
            else:
                mult*=nums[i]
        
        if zeros>=2:
            return ans
        elif zeros==1:
            ans[index]=mult
            return ans

        for i in range(len(nums)):
            ans[i]=(mult//nums[i])

        return ans