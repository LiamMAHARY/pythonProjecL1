# # 1
# matrix = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20],
#     [21, 22, 23, 24, 25]
# ]
# for row in matrix:
#     for cal in row:
#         print(cal, end=" ")
#     print()
# #2
# matrix = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20],
#     [21, 22, 23, 24, 25]
#     ]
# sum1=0
# sum2=0
#
# for row in matrix:
#     sum1=sum(row)
#     sum2+=sum1
# print(sum2)
# #3
# matrix = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20],
#     [21, 22, 23, 24, 25]
# ]
# sum=0
# for row in range(len(matrix)):
#     for cal in range(len(matrix[row])):
#         if cal==row:
#             sum+=matrix[row][cal]
# print(sum)
# #4
# import random
# arry1=[]
# arry2=[[0]*3]*3
# print(arry2)
#
# for i in range(3):
#     u=[]
#     for j in range(3):
#         u.append(random.randint(0, 9))
#     arry1.append(u)
#
#
# print(arry1)
#
# for row in range(3):
#     for cal in range(3):
#         arry2[row][cal]=arry1[cal][row]
# print(arry2)
#
# import random
# arry1=[]
# arry2=[[0]*3]*3
# for row in arry2:
#     print(row)
#
# print()
#
# for i in range(3):
#     u=[]
#     for j in range(3):
#         u.append(random.randint(0, 9))
#     arry1.append(u)
# for row in arry1:
#     print(row)
#
# print()
#
# for row in range(3):
#     for cal in range(3):
#         # z=row
#         # row=cal
#         # cal=z
#         arry2[cal][row]=arry1[row][cal]
#
#
# for row in arry2:
#     print(row)
# print()
# #5
# matrix = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 10],
#     [11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20],
#     [21, 22, 23, 24, 25]
# ]
# for i in range(1, len(matrix), 2):
#     for row in matrix:
#         matrix[i].reverse()
#
# for row in matrix:
#     for cal in row:
#         print(cal, end=" ")
#     print()
# #6
# vip_=["bar", "ofir", "neta"]
# fam_=["avirm", "ohad"]
# friends_= ["motti", "liron", "roni"]
# guests=[
#     vip_,
#     fam_,
#     friends_
# ]
#
# for row in guests:
#     print(row)
#
# out=input("Who would you like to remove?")
# vip_.remove(out)
#
# inside=input("Who would you like to add?")
# friends_.append(inside)
#
# guests=[
#     vip_,
#     fam_,
#     friends_
# ]
# for row in guests:
#     print(row)
# 7
# metrix = []
# tur = []
# add = 1
# num = int(input("length of metrix"))
# for i in range(num):
#     for i in range(num):
#         tur.append(add)
#         add += 1
#     metrix.append(tur)
#     tur = []
# for e in metrix:
#     print(e)
# print()
# metrix1 = list(zip(*reversed(metrix)))
# for e in metrix1:
#     print(e)
# print()
# #8
#
# #9
# list1=[]
# WORKING_SCREEN = "work"
# FAULTY_SCREEN = "problem"
# tv = [
#     [WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN],
#     [WORKING_SCREEN, WORKING_SCREEN, FAULTY_SCREEN, WORKING_SCREEN, WORKING_SCREEN],
#     [WORKING_SCREEN, FAULTY_SCREEN, FAULTY_SCREEN, WORKING_SCREEN, WORKING_SCREEN],
#     [WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, FAULTY_SCREEN, WORKING_SCREEN],
#     [WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, WORKING_SCREEN, FAULTY_SCREEN]
#     ]
# for i in range(len(tv)):
#     for j in range(len(tv[i])):
#         if FAULTY_SCREEN==tv[i][j]:
#             ind=[ i, j]
#             list1.append(ind)
# print(list1)
# 10
restaurant_layout = [
    [4, 2, 6, 3],
    [8, 3, 2, 5],
    [5, 7, 3, 6],
    [9, 4, 2, 8]
]
print("yht")
reservations = [
    ["Group A", 3],
    ["Group B", 6],
    ["Group C", 2],
    ["Group D", 7],
    ["Group E", 5],
    ["Group F", 4],
    ["Group G", 8],
    ["Group H", 3],
    ["Group I", 9],
    ["Group J", 6]
]
for i in restaurant_layout:
    for j in i:
        if j in reservations:
            y=restaurant_layout.index(j)
            x=restaurant_layout.index(i)
            restaurant_layout[x][y]="jjjjj"
        else:
            y = restaurant_layout.index(j)

            restaurant_layout[x][y] = "ii"
