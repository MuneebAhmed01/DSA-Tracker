class Solution:
 def minimumSize(self,A, k):
    left, right = 1, max(A)
    while left < right:
        mid = (left + right) // 2
        splits = 0
        for a in A:
           splits += (a - 1) // mid
        if splits > k:
            left = mid + 1  
        else:
            right = mid
    return left