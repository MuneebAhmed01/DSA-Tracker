class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        for n in nums:
            if n>=0:
                pos.append(n)
            else:
                neg.append(n)
        nums.clear()
        i,j=0,0
        while i<len(pos) or j<len(neg):
            nums.append(pos[i])
            nums.append(neg[j])
            i+=1
            j+=1
        return nums
