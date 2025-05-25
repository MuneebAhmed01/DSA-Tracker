def sort(array):
    nonzeroindex = 0
    for i in range(len(array)):
        if array[i] != 0:
            array[i],array[nonzeroindex]=array[nonzeroindex],array[i]
            nonzeroindex += 1
            
    return array










array=[1,2,4,5,6,8,34,0,4,6,0,3,0,2,0,34,0,5,0,6,0]
print(sort(array))

# py move0toend.py
# def sort(array):
#     result = []
#     for i in range(len(array)):
#       if array[i]!=0:
#         result.append(array[i])
#     zero_length=len(array)-len(result)
#     result.extend([0] * zero_length)
#     return result












# array=[1,2,4,5,6,8,34,0,4,6,0,3,0,2,0,34,0,5,0,6,0]
# print(sort(array))

# # py move0toend.py