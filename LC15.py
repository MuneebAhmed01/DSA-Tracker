class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i,n in enumerate(nums):
            if i>0 and n==nums[i-1]:
                continue
            start=i+1
            end=len(nums)-1
            while start<end:
                threeSum=n+nums[start]+nums[end]
                if threeSum>0:
                    end-=1
                elif threeSum<0:
                    start+=1
                else:
                    res.append([n,nums[start],nums[end]])
                    start+=1
                    while nums[start]==nums[start-1] and start<end:
                        start+=1
        return res



            
            


            
            