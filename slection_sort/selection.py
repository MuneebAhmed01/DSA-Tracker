# array1 = [19,81,93,34,12,13]
# n= len(array1)
# for i in range(0,len(array1)-2):
#     min_index = array1[1]
#     for j in range(i +2 , n):
#         if array1[j] < min_index:
#             min_index= array1[j]
#     print(array1)





# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_index = i  # Assume current index is minimum
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j  # Update min_index if smaller found
#         arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap
#     return arr


# arr = [12, 43, 53, 54, 24]
# sorted_arr = selection_sort(arr)
# print(sorted_arr)









# def fruit_sort(fruits):
#     n = len(fruits)
#     for i in range(n):
#         min_index = i  # was min_len = len(fruits[i])
#         for j in range(i+1, n):
#             if len(fruits[j]) < len(fruits[min_index]):
#                 min_index = j  # fixed logic to use index
#         fruits[i], fruits[min_index] = fruits[min_index], fruits[i]  # moved out of inner loop
#     return fruits  # moved return outside the loop

# fruits = ["apple", "mango", "guava", "pea", "banana", "pineapple"]
# sor = fruit_sort(fruits)
# print(sor)









# def tuple_sort(tuple):
#     n = len(tuple)
#     for i in range(n):
#         min_length = i
#         for j in range(i+1,n):
#             if tuple[j][1] < tuple[min_length][1]:
#                 min_length = j
#         tuple[i],tuple[min_length]=tuple[min_length],tuple[i]
#     return tuple
            

# data = [(21,12),(2,24),(3,2)]
# soeted_data = tuple_sort(data)
# print(soeted_data)




# def student_data(marks):
#     n =len(marks)
#     for i in range(n):
#      min_marks = i
#      for j in range(i+1,n):
#         if marks[j]["marks"]<marks[min_marks]["marks"]:
#            min_marks = j
#      marks[i],marks[min_marks] = marks[min_marks],marks[i]
#     return marks



# students = [
#     {"name": "Ali", "marks": 76},
#     {"name": "Zara", "marks": 9},
#     {"name": "Babar", "marks": 65}
# ]
# data = student_data(students)
# print(data)












def sorted_marks(marks):
    n = len(marks)
    for i in range(n):
       
        for j in range(0,n-i-1):
            if marks[j+1]<marks[j]:
                
             marks[j],marks[j+1]=marks[j+1],marks[j]
    return marks



marks = [12,90, 45, 89, 23, 12 ]
result = sorted_marks(marks)
print(result)


