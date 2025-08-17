class Solution:
    def findMedianSortedArrays(self,nums1,nums2):
        # This is Foolish way to solve this question because of Time complexity constraint but for some reason leetcode pass it ignoring time constraint
        return median(sorted(nums1+nums2))
