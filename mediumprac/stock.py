def stock(arr):
    min_price=float('inf')
    max_price=0
    buydy=0
    sellday=0
    for i,num in enumerate(arr):
        print(min_price)
        if num<min_price:
            min_price=num
            buydy=i
        elif num-min_price>max_price:
            max_price = num
            sellday = i
            print(sellday)
    return max_price,buydy,sellday


arr=[2,3,4,1,9,8,12]
print(stock(arr))

#failed to understand it correctly