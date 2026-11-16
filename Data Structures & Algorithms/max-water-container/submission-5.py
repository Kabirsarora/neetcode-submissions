class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right=len(heights)-1
        left=0
        ans=0
        while left<right:
            if heights[right]>heights[left]:
                ans=max(ans,(right-left)*min(heights[right],heights[left]))
                left+=1
            else:
                ans=max(ans,(right-left)*min(heights[right],heights[left]))
                right-=1

        return ans