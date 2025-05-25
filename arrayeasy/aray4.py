def shift_right(arr):
    if len(arr) == 0:
        return arr  # Empty list, nothing to shift

    last = arr[-1]  # Save the last element
    for i in range(0,len(arr) - 1):
        arr[i] = arr[i - 1]  # Shift each element to the right
    arr[0] = last  # Place last element at the front
    return arr

arr = [1, 21, 23, 14, 51]
shifted = shift_right(arr)
print(shifted)



def shift_right(arr):
    if len(arr) == 0:
        return arr  # Empty list, nothing to shift

    last = arr[-1]  # Save the last element
    for i in range(0,len(arr) - 1):
        arr[i] = arr[i - 1]  # Shift each element to the right
    arr[0] = last  # Place last element at the front
    return arr

arr = [1, 21, 23, 14, 51]
shifted = shift_right(arr)
print(shifted)