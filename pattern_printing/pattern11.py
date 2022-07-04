# space=7
# for i in range(7):
#     for j in range(space):
#         print(end=' ')
#     space=space-1
#     for k in range(i):
#         print('*',end=' ')
#     print()
# space=2
# for i in range(5,0,-1):
#     for j in range(space):
#         print(end=' ')
#     space+=1
#     for k in range(i):
#         print('*',end=' ')
#     print()
space=1
for i in range(6,0,-1):
    for j in range(space):
        print(end=' ')
    space+=1
    for k in range(i):
        print('*',end=' ')
    print()
space=6
for i in range(1,7):
    for j in range(space):
        print(end=' ')
    space=space-1
    for k in range(i):
        print('*',end=' ')
    print()
