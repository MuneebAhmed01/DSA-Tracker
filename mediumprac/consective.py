def cons(arr):
    st = set()
    longest=1
    for i in range(len(arr)):
        st.add(arr[i])
    for num in st:
        if num-1 not in st:
            cnt=1
            x=num
            while x+1 in st:
             cnt+=1
             x+=1
             longest=max(longest,cnt)
    return longest


arr=[6,2,3,4,8,9,10,12,4,5]
print(cons(arr))