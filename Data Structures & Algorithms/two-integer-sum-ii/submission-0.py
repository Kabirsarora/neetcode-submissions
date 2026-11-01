from collections import defaultdict
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a=defaultdict(int)

        for i in range(len(numbers)):
            curr=target-numbers[i]
            if curr in a:
                return [a[curr]+1,i+1]
            else:
                a[numbers[i]]=i

