space=5
for i in range(5):
    for k in range(space):
        print(end=' ')
    space-=1
    for j in range(i):
        print('*',end=' ')
    print()
space=0
for i in range(5,0,-1):
    for k in range(space):
        print(end=' ')
    space+=1
    for j in range(i):
        print('*',end=' ')
    print()