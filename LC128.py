class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        largest=0
        for num in num_set:
            if num-1 not in num_set:
                main=num
                count=1
                while main+1 in num_set:
                    count+=1
                    main+=1
                largest=max(count,largest)
        return largest