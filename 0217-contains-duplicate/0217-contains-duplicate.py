class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        return True if [k for k in nums if freq[k]>1] else False
