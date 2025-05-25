def unique(arr):
    xor=0
    for i in range(len(arr)):
        xor ^= arr[i]
    return xor



arr=[1,2,3,4,4,3,2,1,3]
print(unique(arr))