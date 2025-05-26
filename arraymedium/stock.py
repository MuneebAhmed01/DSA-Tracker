def stock(arr):
    min_price=float('inf')
    max_profit=0
    buyday=-1
    sellday=-1
    
    for i,num in enumerate(arr):
        
         if num<min_price:
            min_price = num
            buyday=i
         elif num-min_price>max_profit:
            max_profit=num-min_price
            sellday=i

           
    return sellday,buyday,max_profit



        


arr=[1,5,6,7,8,1,9]
print(stock(arr))