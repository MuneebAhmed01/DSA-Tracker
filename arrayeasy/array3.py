#check for duplicate


def sort_check(arr):
    new_arr = []
    for i in range(len(arr) - 1):
        if arr[i] != arr[i + 1]:
            new_arr.append(arr[i])
    new_arr.append(arr[-1])  # Always include the last element
    return new_arr

arr = [1,2,3,4,4,4,4,5,6,5,6,7,8,9,9,9,9]
check_sort = sort_check(arr)
print(check_sort)
