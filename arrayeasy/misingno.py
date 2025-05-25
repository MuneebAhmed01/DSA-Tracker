def missing_number_sum(arr):
    n = len(arr) + 1
    total_sum = n * (n + 1) // 2
    actual_sum = 0
    for num in arr:
        actual_sum += num
    return total_sum - actual_sum



arr = [1,4 ,3, 5] 

print(missing_number_sum(arr))  
