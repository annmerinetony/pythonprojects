a={1,2,3,4,5}
b={1,3,5,6,7,8,9}
common=set()
for i in a:
    if i in b:
        common.add(i)
print(common)