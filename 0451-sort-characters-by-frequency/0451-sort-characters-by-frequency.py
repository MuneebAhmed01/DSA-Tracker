class Solution(object):
   def frequencySort(self, s):
       d={}
       for i in s:
           d[i]=d.get(i,0)+1
       s=sorted(d.items(),key=lambda x:x[1],reverse=True)#sorting our dictionary in terms of keys
       r=""
       for c,f in s:
           r+=c*f
       return r

        