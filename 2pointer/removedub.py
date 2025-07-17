


def dub(arr):
    res=[arr[0]]
    for i in range(1,len(arr)):
        if arr[i]!=res[-1]:
            res.append(arr[i])
    return res










arr=[1,1,1,1,1,2,2,2,4,4,4,6,6,7,7,9]
print(dub(arr))