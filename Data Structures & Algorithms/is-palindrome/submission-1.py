class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s=s.lower()
        l,r=0,len(s)-1
        while l<r:
            if s[l]!=s[r]:
                return False
                
            r-=1
            l+=1
        
        return True