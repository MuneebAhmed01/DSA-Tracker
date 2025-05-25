# def twosum(array):
#     target = int(input("Enter your number"))
#     for i in range(len(array)):
#         for j in range(i+1,len(array)):
#          if array[i]+array[j] == target:
#             print(i,j)
#             return True
        
#     print("false")







# array = [1,3,5,7,9]
# solution = twosum(array)
# print(solution)


def twoSum(nums, target):
    seen = {}  # number -> index mapping
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i


nums = [1,22,4,9,3,5,7,12]
target = int(input("Enter number"))
solution = twoSum(nums,target)
print(solution)
