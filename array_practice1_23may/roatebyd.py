#Left rotate an array by D places
def reverse(arr,start,end):
    while start < end:
        arr[start],arr[end]=arr[end],arr[start]
        start +=1
        end -=1
    return arr


def rotatebyd(arr,d):

    
    reverse(arr,0,d-1)
    
    reverse(arr,d,len(arr)-1)

    reverse (arr,0,len(arr)-1)
    return arr





d=4
arr=[1,2,3,4,5,6,7]
print(rotatebyd(arr,d))


#i didnt use d=d%n which is useful and optimal or larger d also i use != instead of < whoich cause error and gpt help me solve it