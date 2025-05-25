def slargest(arr):
    
    slarge=0
    large = 0
    for i in range(len(arr)-1):
     if arr[i]>arr[i+1]:
      large = arr[i]
      slarge=arr[i+1]
    return slarge



arr=[1,2,3,4,5,6]
print(slargest(arr))