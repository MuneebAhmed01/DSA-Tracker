class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count,edge=0,0
        for n in nums:
            if n==1:
                count+=1
            else:
                if count>edge:
                 edge=count
                count=0
        return max(count,edge)
        