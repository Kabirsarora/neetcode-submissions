from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        counter=-1
        ans=[]
        diff=defaultdict(int)
        for i in range(len(strs)):
            a = tuple(sorted(strs[i]))
            if a in diff:
                d=diff[a]
                ans[d].append(strs[i])
            else:
                counter+=1
                diff[a]=counter
                ans.append([strs[i]])

        return ans