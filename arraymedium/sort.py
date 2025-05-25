# def merge_sort(array):
#     if len(array)<=1:
#         return array
#     mid = len(array) //2
#     left_side = array[:mid]
#     right_side = array[mid:]

#     left_sorted=merge_sort(left_side)
#     right_sorted = merge_sort(right_side)

#     return merge(left_sorted,right_sorted)

# def merge(left,right):
#     result = []
#     i=j=0
#     while i < len(left) and j < len(right):
#      if left[i]<right[j]:
#         result.append(left[i])
#         i +=1
#      else:
#         result.append(right[j])
#         j+=1
    
#     result += left[i:]
#     result += right[j:]
#     return result

# array = [0,1,2,1,1,2,0,2,0,1,0,2,2,1,1,0,1]
# solution = merge_sort(array)
# print(solution)


def sort(arr):
    low=0
    mid=0
    high=len(arr)-1
    while mid<= high:
        if arr[mid]==0:
            arr[mid],arr[low]=arr[low],arr[mid]
            low+=1
            mid+=1
        elif arr[mid]==2:
            arr[mid],arr[high]=arr[high],arr[mid]
            high-=1
        elif arr[mid] == 1:
            mid += 1
    return arr




# Test case to sort an array containing 0s, 1s, and 2s using the sort function
print(sort([0,1,2,1,1,2,0,2,0,1,0,2,2,1,1,0,1]))