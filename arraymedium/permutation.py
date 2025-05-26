def next_per(num):
    n=len(num)
    i=n-2
    while i>=0 and num[i]>=num[i+1]:
        i-=1
    if i>=0:
        j=n-1
    while num[i]<=num[j]:
        j-=1
    num[i],num[j]=num[j],num[i]

    left,right=i+1,n-1
    while left<right:
        num[left],num[right]=num[right],num[left]
        left+=1
        right-=1
    return num


num=[1,2,3,4,2]
print(next_per(num))