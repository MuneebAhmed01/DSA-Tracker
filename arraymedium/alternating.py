def alternating(arr):
    
   pos = []
   neg = []
   for num in arr:
     if num>=0:
       pos.append(num)
     else:
       neg.append(num)

   Result = []
   i=j=0
   while i<len(pos) and j<len(neg):
     Result.append(neg[j])
     Result.append(pos[i])
     i+=1
     j+=1
#    while i<len(pos):
#      Result.append(pos[i])
#      i=+1
#    while j<len(neg):
#      Result.append(neg[j])
#      j+=1
   return Result
    
     
        



arr=[1,2,3,-1,-2,-3]
print(alternating(arr))
# py alternating.py