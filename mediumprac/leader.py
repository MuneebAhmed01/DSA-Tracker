# def leader(arr):
#     res=[]
#     n=len(arr)
#     last=arr[-1]
#     for i in range(0,n-1):
#         isleader=True
#         for j in range(i,n):
#             if arr[i]<arr[j]:     
#              isleader=False
#         if isleader:
#             res.append(arr[i])

             
    
#     res.append(last)
#     return res



# arr=[7,3,5,3,5,8,1,2,3]
# print(leader(arr))

def leader(arr):
    res = []
    max_from_right = arr[-1]
    res.append(max_from_right)

    for i in range(len(arr) - 2, -1, -1):
        if arr[i] > max_from_right:
            max_from_right = arr[i]
            res.append(arr[i])
    
    return res[::-1]  # Reverse the result to maintain original order

arr=[7,3,5,3,5,8,1,2,3]
print(leader(arr))

