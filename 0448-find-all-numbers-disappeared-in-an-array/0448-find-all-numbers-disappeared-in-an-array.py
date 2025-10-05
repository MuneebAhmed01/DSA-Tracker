class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        freq={}
        res=[]
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for i in range(1,len(nums)+1):
            if freq.get(i, 0) == 0:
                res.append(i)
        return res

        
        