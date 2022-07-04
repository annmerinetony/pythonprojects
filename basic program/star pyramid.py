# def pymid(r):
#     for i in range(r):
#         print(" "*(r-i-1)+"*"*(2*i+1))
# pymid(4)
# pymid(6)

for i in range(5):
    for j in range(i):
        print("*",end=" ")
    print("\r")
for i in range (4,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()

for i in range (4,0,-1):
    for j in range(i):
        print("*", end=" ")
#     print()
for i in range(5):
    for j in range(5-i):
        print(end=" ")
    for k in range(i):
        print("*",end=" ")
    print()
for i in range (4,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(5):
    for j in range(i):
        print(j,end=" ")
    print("\r")
#
# for i in range(7):
#     num=0
#     for j in range(i):
#         print(num,end=" ")
#         num=num+1
#     print("\r")
#
# for i in range(5):
#     for j in range(i):
#         print(i-1,end=" ")
#     print("\r")
#
#
