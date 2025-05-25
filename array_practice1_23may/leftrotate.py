def rotate(a):
    left = a[0]
    for i in range(len(a)-1):
        a[i]=a[i+1]
    a[-1]=left
    return a


a=[1,2,3,4,5]
print(rotate(a))

#i put a[-1] inside due due to which i was getting error,use gpt hint,overall good effort