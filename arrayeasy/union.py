def find_array_intersection(A, B, n, m):
    i = 0
    j = 0
    ans = []
    while i < n and j < m:
        if A[i] < B[j]:
            i += 1
        elif B[j] < A[i]:
            j += 1
        else:
            ans.append(A[i])
            i += 1
            j += 1
    return ans


A=[1,2,3,4,5,6,7,8]
B= [4,5,5,6,7,8,8,9]
n=len(A)
m=len(B)
print(find_array_intersection(A,B,n,m))