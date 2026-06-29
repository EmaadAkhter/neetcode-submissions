class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        m=-1
        while l<r:
            nm=min(heights[l],heights[r])*(r-l)

            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1

            m=max(m,nm)
        
        return m
        