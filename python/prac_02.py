# from python.prac_01 import num;
# # num(101)

# steric right angle triangle
# number = int(input("pelase enter the number:"))
# for i in range(0,number + 1):
#     for j in range(0,i):
#         print("*", end="")
#     print("")


# steric square box
# number = int(input("pelase enter the number:"))
# for i in range(0,number):
#     for j in range(0,number):
#         print("*", end="")
#     print("")




# # number right angle triangle
# number = int(input("pelase enter the number:"))
# for i in range(0,number + 2):
#     for j in range(0,i):
#         print(j, end="")
#     print("")

# #  same number row right angle triangle
# number = int(input("pelase enter the number:"))
# for i in range(0,number + 1):
#     for j in range(0,i):
#         print(i, end="")
#     print("")


# upside down left Ngle triangle
# number = int(input("pelase enter the number:"))
# for i in range(0,number):
#     for j in range(i,number):
#         print("*", end="")
#     print("")


# number = int(input("Please Enter Your Number : "))
# for i in range(0, number + 2):
#     for j in range(1,(number + 1) - i):
#         print(j,end="")
#     print("")    


number = int(input("Please Enter Your Number : "))
for i in range(1, number+1):
    for j in range((number - i)):
        print(" ",end="")
    for k in range(i*2 -1):
        print("*",end="")
    for l in range(i-1):
        print(" ",end="")
    for m in range(2 * (number - i) +1):
        print("*",end="")
    print("")  


# number = int(input("Please Enter Your Number : "))
# for i in range(1, number+1):
#     for j in range(i-1):
#         print(" ",end="")
#     for k in range(2 * (number - i) +1):
#         print("*",end="")
    
#     print("")    





#Continue From 10 Onward