class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre={}
        out=[]
        for n in nums:
            fre[n]=fre.get(n,0)+1


        s_fre = sorted(fre, key=fre.get, reverse=True)

        return s_fre[:k]
        