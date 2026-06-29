class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        t=list(t)
        s=list(s)
        for i in s:
            if i in t:
                t.remove(i)
            else:
                return False
        
        if t is None:
            return false
        
        return True