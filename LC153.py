class Solution:
    def findMin(self, nums: List[int]) -> int:
        start=0
        end=len(nums)-1
        smallest=nums[0]
        while start<=end:
            mid=(start+end)//2
            
        # if nums is rotated
            if nums[start]>nums[end]<nums[mid]:
                start=mid+1
            else:
                end=mid-1
            smallest=min(smallest,nums[mid])
        return smallest
            