class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        l=0
        m_l=0
        m_f=0 

        for r in range(len(s)):
            
            count[s[r]]=1+count.get(s[r],0)

            m_f=max(m_f,count[s[r]])

            if (r-l+1)-m_f>k:
                count[s[l]]-=1
                l+=1
            
            m_l = max(m_l, r - l + 1)
            
        return m_l
