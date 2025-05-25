def consective(arr):
    count =0
    cons_one = 0
    for i in range(len(arr)):
        if arr[i]==1:
            count+=1
        else:
            count = 0
        if count>cons_one:
            cons_one=count
    return cons_one



arr=[1,1,2,2,2,2,3,1,1,1]
print(consective(arr))