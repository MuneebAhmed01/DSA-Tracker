def linear(array,target):
    
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1







target=int(input("Enter NUmber"))
array=[1,2,3,4,5,6,7,8]
print(linear(array,target))