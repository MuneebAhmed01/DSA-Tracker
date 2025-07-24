class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def reverse_array(nums,start,end):

            while start<=end:
                nums[start],nums[end]=nums[end],nums[start]
                start+=1
                end-=1
            return nums
        start=0
        end=len(nums)-1
        k = k % len(nums)
        reverse=reverse_array(nums,start,end)
        reverse_k=reverse_array(reverse,start,k-1)
        reverse_sol=reverse_array(reverse_k,k,end)