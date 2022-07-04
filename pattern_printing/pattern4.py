for i in range(5):
    for j in range(i):
        print(i-1,end=" ")
    print("\r")

num=0
for i in range(5):
    for j in range(i):
        print(num-1,end=" ")
    num=num+1
    print("\r")

num=0
for i in range(4):
    for j in range(-1,i):
        print(num,end=" ")
    num=num+1
    print("\r")

for i in range(5):
    for j in range(i):
        print(i,end=" ")
    print("\r")

# 0
# 1 1
# 2 2 2
# 3 3 3 3