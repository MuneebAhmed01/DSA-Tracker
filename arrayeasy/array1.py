#fin second largest element in arrray__

#this is brute force

def merge_sort(array):
    if len(array)<=1:
        return array
    mid = len(array)//2
    left_half = array[:mid]
    right_half = array[mid:]
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    return merge(left_sorted,right_sorted)


def merge(left,right):
    result= []

    i = j = 0



    while i < len(left) and j < len(right):
      if left[i] < right[j]:
        result.append(left[i])
        i +=1
      else:
        result.append(right[j])
        j+=1
    result += left[i:]
    result += right[j:]
    return result
    

array = [1,31,4,5,6,11,2,3,7,9]
sorted_array = merge_sort(array)
print(sorted_array[-2])

#optimal

def secondSmallest(arr, n):
    if (n < 2):
        return -1
    small = float('inf')
    second_small = float('inf')
    for i in range(n):
        if (arr[i] < small):
            second_small = small
            small = arr[i]
        elif (arr[i] < second_small and arr[i] != small):
            second_small = arr[i]
    return second_small