
def removeDuplicates(num):
  if len(num)<=1:
    return num

  result = [num[0]]
  for i in range(len(num)):
    if num[i] != result[-1]:
      result.append(num[i])
  return result

num = [0,0,0,1,1,1,2,2,2,2,2,3,3,4,5,6,7,7,7,7]
sol = removeDuplicates(num)
print(sol)