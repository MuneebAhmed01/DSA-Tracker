class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=0
        right=len(nums)-1
        def binary(left,right,target,bias):
            ans=-1
            while left<=right:
                mid=(left+right)//2
                if target==nums[mid]:
                    ans=mid
                    if bias:
                        right=mid-1
                    else:
                        left=mid+1
                elif target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            return ans
            
            
        
                        

        leftbias=binary(left,right,target,True)
        rightbias=binary(left,right,target,False)
        return leftbias,rightbias