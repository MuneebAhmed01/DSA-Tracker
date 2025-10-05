class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp=sorted(nums)
        d={}
        res=[]
        for i,n in enumerate(temp):
            if n not in d:
                d[n]=i
        for i in nums:
            res.append(d[i])
        return res