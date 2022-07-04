# a=[8,5,2,1,44,99,2.5,False]
# a.sort()
# print(a)
# def bs(a):
#     b=len(a)-1
#     for i in range (b):
#         for j in range (b-i):
#             if a[j]>a[j+1]:
#                 a[j],a[j+1]=a[j+1],a[j]
#     return a
# a=[4,11,9,2,7]
# print(len(a))
# print(bs(a))
# print(a[-1])
a=[8,5,2,1,44,99,2.5,False]
b=len(a)-1
for i in range (b):
     for j in range (b-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)
a=[8,5,2,1,44,99]
b=len(a)-1           #5
for i in range(b):             #0,1,2,3,4
     for j in range(b-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)


a=[8,5,2,1,44,99]
new_list=[]
while a:
    min=a[0]
    for i in a:
        if i<min:
            min=i
    new_list.append(min)
    a.remove(min)
print(new_list)
