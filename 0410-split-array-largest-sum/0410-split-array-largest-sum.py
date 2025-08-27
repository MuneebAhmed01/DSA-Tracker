class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def countpartition(nums,mid):
            partition=1
            maxsubarray_sum=0
            for i in range(len(nums)):
                if maxsubarray_sum+nums[i]<=mid:
                    maxsubarray_sum += nums[i]
                else:
                    partition += 1
                    maxsubarray_sum = nums[i]
            return partition
        


        start=max(nums)
        end=sum(nums)
        while start<=end:
            mid=(start+end)//2
            partitions=countpartition(nums,mid)
            if partitions>k:
                start=mid+1
            else:
                end=mid-1
        return start
        