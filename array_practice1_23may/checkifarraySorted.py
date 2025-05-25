#Check if the array is sorted
def sort(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return "not sorted"
    return "sorted"



arr=[1,2,3,4,4,5]
print(sort(arr))

#done on first try yesh
