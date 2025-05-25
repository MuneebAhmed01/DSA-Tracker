#Majority Element (>n/2 times)
def majority(arr):
    count = 0
    candidate = 0
    for num in arr:
        if count ==0:
          num = candidate
        count += (1 if num==candidate else -1)
    return candidate


arr =[2,2,5,2,4,2]
print(majority(arr))