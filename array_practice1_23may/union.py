#	Find the Union
def union(arr1,arr2):
    result=[]
    for element in arr1:
        if element not in result:
            result.append(element)
    for element in arr2:
        if element not in result:
            result.append(element)
    return result
    



arr1=[1,2,3,5,6,7,8]
arr2=[2,3,4,5,7,6]
print(union(arr1,arr2))

#full copy paste