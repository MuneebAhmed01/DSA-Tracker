#Remove duplicates from Sorted array
def removedub(arr):
    result = [arr[0]]
    for i in range(len(arr)):
        if arr[i] != result[-1]:
            result.append(arr[i])
    return result



arr=[1,1,2,2,2,2,2,3,3,4,6,6,6,6,6,6,7]
print(removedub(arr))

#very small mistake out of index so i put result=[arr[i]] ,i got it myself without Ai
