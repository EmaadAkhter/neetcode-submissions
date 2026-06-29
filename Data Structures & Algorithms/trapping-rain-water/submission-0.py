class Solution:
    def trap(self, height: List[int]) -> int:

        l,r=0,len(height)-1
        leftm,rightm=height[l],height[r]
        res=0

        while l<r:
         if leftm<rightm:
             l+=1
             leftm=max(leftm,height[l])
             res+=leftm-height[l]        
         else:
             r-=1
             rightm=max(rightm,height[r])
             res+=rightm-height[r]        
         
        return res
            
        