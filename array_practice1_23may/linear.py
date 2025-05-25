#Linear Search
def linear(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return "-1"




target = int(input("Enter YOur Number : "))
arr=[1,2,3,4,5,6]
print(linear(arr,target))

#done on first try