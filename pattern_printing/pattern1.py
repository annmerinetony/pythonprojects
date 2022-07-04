# def pymid(r):
#     for i in range(r):
#         print(" "*(r-i-1)+"*"*(2*i+1))
# # pymid(4)


# r=4
# for i in range(r):
#     print(" " * (r - i - 1) + "*" * (2 * i + 1))
# #


# for i in range(r):
#     print(" " * (r - i - 1) + "*" * (2 * i ))


space=5
for i in range(5):
    for j in range(space):
        print(end=" ")
    space-=1
    for k in range(i):
        print("*",end=" ")
    print()


for i in range(5):
    for j in range(5-i):
        print(end=" ")
    for k in range(i):
            print("*",end=" ")
    print()

for i in range(5):
    print("  "* (5-i-1)+"* "*(2*i+1))