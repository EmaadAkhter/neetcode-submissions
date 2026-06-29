class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        perview={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in perview:
                return [perview[diff],i]
            
            perview[n]=i



        """    for i in range(len(nums)):
            ans=target-nums[i]
            if ans in nums:
                idx=nums.index(ans)
                if idx != i:
                    if i>=idx:
                        return [idx,i]
                    else:
                        return [i,idx]
        """         
        