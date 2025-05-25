#Move Zeros to end
def move0toend(arr):
    nonzeroindex = 0
    for i in range(len(arr)-1):
     if arr[i]!=0:
        arr[i],arr[nonzeroindex]=arr[nonzeroindex],arr[i]
        nonzeroindex+=1

    return arr

arr=[1,0,2,2,3,4,0,0,5,4,0,5,0]
print(move0toend(arr))

#failed to solve by myself