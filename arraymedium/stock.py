def stock(arr):
    largest= 0
    smallest = arr[0]
    for i in range(len(arr)):
        if arr[i]>largest:
            largest = i
        if arr[i]<smallest:
            smallest=i
    return f"The best day to buy is day {smallest} and the day to sell is day {largest}"

    

        


arr=[3,5,6,7,8,1,4]
print(stock(arr))