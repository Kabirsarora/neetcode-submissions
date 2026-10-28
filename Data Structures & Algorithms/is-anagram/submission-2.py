from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter=defaultdict(int)
        if len(s)!=len(t):
            return False

        for i in range(len(s)):
            counter[s[i]]+=1
            counter[t[i]]-=1

        for key in list(counter.keys()):
            if counter[key] == 0:
                del counter[key]

        if len(counter)==0:
            return True
        
        return False
         

        
