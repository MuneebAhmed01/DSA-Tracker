class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq={}
        for n in nums:
           freq[n] = freq.get(n, 0) + 1

        return True if [n for n in freq if freq[n]>1] else False