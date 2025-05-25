#better time complexity
#use recursion
#lil more difficult than previous sorting algo
#divide and merge algo


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Step 1: Divide the array
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Step 2: Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Step 3: Merge the sorted halves
    return merge(left_sorted, right_sorted)

# Helper function to merge two sorted arrays
def merge(left, right):
    result = []
    i = j = 0

    # Compare and merge
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements (if any)
    result += left[i:]
    result += right[j:]
    
    return result

# Example usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print(sorted_arr)
