def max_subarray(nums):
    max_sum = float('-inf')
    current_sum = 0
    
    start = 0      # potential start index of current subarray
    max_start = 0  # start index of max subarray found
    max_end = 0    # end index of max subarray found
    
    for i, num in enumerate(nums):
        if current_sum <= 0:
            # start new subarray here
            start = i
            current_sum = num
        else:
            current_sum += num
        
        # update max if current_sum is better
        if current_sum > max_sum:
            max_sum = current_sum
            max_start = start
            max_end = i
    
    # return max sum and the subarray with max sum
    return max_sum, nums[max_start:max_end+1]

nums=[2,2,4,2,-6,2,-9,2,2,2]
print(max_subarray(nums))