def alter(arr):
    res=[]
    pos=[]
    neg=[]
    for num in arr:
        if num<0:
            neg.append(num)
        else:
            pos.append(num)
    i=j=0
    while i<len(pos) and j<len(neg):
        res.append(neg[i])
        res.append(pos[i])
        i+=1
        j+=1
    return res



arr=[-1,2,-3,4,-5,6,-7,8,-9,10]

print(alter(arr))

#good effort,understand the logic of it