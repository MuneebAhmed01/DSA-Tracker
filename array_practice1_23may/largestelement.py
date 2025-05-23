#Find Largest Element In Array
def largest(arr):
    largest = arr[0]
    for i in range(len(arr)):
        if arr[i]>largest:
            largest = arr[i]
    return largest



arr=[1,2,33,4,5,6,22,3,4]
print(largest(arr))

#optimal done on first try.Nice