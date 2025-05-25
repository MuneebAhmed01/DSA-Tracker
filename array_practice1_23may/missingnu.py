# Find missing number in an array
def missing(arr):
    n=len(arr)+1
    total_sum = n *(n+1) //2
    actual_sum = 0
    for num in arr:
        actual_sum +=num
    return total_sum-actual_sum
    





arr=[1,2,4,5]
print(missing(arr))

#cant remember formula to count total sum otherwise i understood logic