l=[1,2,3,4,5,6,7,8,3,5,7,1]
D=[]

# for i in l:
#     if i in l:
#         l.remove(i)
#         D.append(i)
# print(l)
# print(D)
for i in l:
    if i==i:
        l.remove(i)
        D.append(i)
print(D)
print(l)
#         break
# else:
#     D.append(i)
#     print(D)
