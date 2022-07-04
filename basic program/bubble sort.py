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

def bs(a):
    b=len(a)-1
    for i in range (b):
        for j in range (b-i):
            if a[j]<a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a
a=[4,11,9,2,7]
print(len(a))
print(bs(a))
print(a[-1])



