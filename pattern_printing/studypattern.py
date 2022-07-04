# 1
# 2 2
# 3 3 3
# 4 4 4 4
for i in range(5):
    for j in range(i):
        print(i,end=" ")
    print()

print()
# 4 4 4 4
# 3 3 3
# 2 2
# 1

for i in range(4,0,-1):
    for j in range(i):
        print(i,end=" ")
    print()
for i in range(4,0,-1):
    for j in range(i):
        print(j,end=" ")
    print()
print()
b=0
for i in range(5,0,-1):
    b=b+1
    for j in range(0,i):
        print(b,end=" ")
    print()
print()
for i in range(6):
    for j in range(i):
        print(j+1,end=" ")
    print()

for i in range(4,0,-1):
    for j in range(i):
        print(5,end=" ")
    print()
print()

for i in range(5,0,-1):
    for j in range(i+1):
        print(j,end=" ")
    print()
print()
num=1
stop=2
for i in range(3):
    for j in range(1,stop):
        print(num,end=" ")
        num+=1
    stop+=2
    print()