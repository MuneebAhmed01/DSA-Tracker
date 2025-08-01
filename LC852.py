class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start=0
        end=len(arr)-1
        while start<=end:
            mid=(start+end)//2
            peak=mid
            if arr[mid+1]>arr[mid]:
               start=mid+1
            else:
               end=mid-1
            if arr[mid+1]>arr[mid]:
                peak=mid+1
            elif arr[mid+1]<arr[mid]:
                peak=mid
            else:
                peak=mid-1
        
        return peak

            
        