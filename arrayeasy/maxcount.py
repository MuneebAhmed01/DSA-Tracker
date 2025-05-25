def max_consecutive_ones_optimal(arr):
    max_count = 0
    count = 0
    for num in arr:
        if num == 1:
            count += 1
            if count > max_count:
                max_count = count
        else:
            count = 0
    return max_count

arr=[1,1,0,0,0,0,0,0,0,0,1,1,1]
print(max_consecutive_ones_optimal(arr))