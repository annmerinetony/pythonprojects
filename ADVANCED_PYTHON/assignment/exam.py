initial=int(input("enter initial range"))
final=int(input("enter final range"))
for n in range(initial):
    for i in range(6):
        for j in range(i):
            print(n+1,end=' ')
        print()
    for i in range(5,0,-1):
        for k in range(i):
            print(n+2, end=' ')
        print()
    for i in range(6):
        for j in range(i):
            print(n+3,end=' ')
        print()
    for i in range(5,0,-1):
        for k in range(i):
            print(n+4, end=' ')
        print()
# initial=int(input("enter initial range"))
# final=int(input("enter final range"))
# for n in range(initial):
#     for i in range(6):
#         for j in range(i):
#             print(n+1,end=' ')
#         print()
#     for i in range(5,0,-1):
#         for k in range(i):
#             print(n+2, end=' ')
#         print()
#     for i in range(6):
#         for j in range(i):
#             print(n+3,end=' ')
#         print()
#     for i in range(5,0,-1):
#         for k in range(i):
#             print(n+4, end=' ')
#         print()
# # #
# list=[1,0,7,5,9,2,3,5,7,2,0,1,10]
# d=[i for i in list if i not in]
# print(d)

# list=[3,5,7,9,0,8,55,34,23,76,4,65,12,89,56,76,34,289,49,12,63,976]
# list.sort()
# # print(list[1])
# s=[('anu',67),('amal',69),('arun',65)]
# a=[]
# b=[]
# for i in s:
#     print(i[0])
#     if i[1]>
#     b.append(i[0])
#     a.append(i[1])
# a.sort()
# print(a)
# print(a[-1])

    # if i[1]
# b=[3,77,0,5,33,6,22,5,90,32,56,78,98,54,67,11,34,88]
# mid=(len(b)-1)//2
# print(b[mid])
# b.remove(b[mid])
# print(b)
#
# a=str(input('enter num'))
# reverse=a[::-1]
# print(reverse)
#
# div=[i for i in range(1,100+1) if i%5==0]
# print(div)
