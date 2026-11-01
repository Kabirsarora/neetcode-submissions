class Solution:
    def isPalindrome(self, s: str) -> bool:
        allowed = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
        right=len(s)-1
        left=0

        while left<right: 
            if s[left] not in allowed and s[right] not in allowed:
                left+=1
                right-=1
            elif s[left] not in allowed:
                left+=1
            elif s[right] not in allowed:
                right-=1
            elif s[left].lower()==s[right].lower():
                left+=1
                right-=1
            else:
                return False
        
        return True