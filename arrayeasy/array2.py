# check if array is sorted

def sort_check(arr):
    
      for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
         return "not sorted"
      return "sorted"










arr = [1,2,3,4,4,4,4,5,6,5,6,7,8,9,9,9,9]
check_sort = sort_check(arr)
print(check_sort)