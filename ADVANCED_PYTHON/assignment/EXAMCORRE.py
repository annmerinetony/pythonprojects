# 1.
# initial=int(input('range1'))
# final=int(input("range2"))
# for i in range (initial,final):
#     if i%2==0:
#         for a in range(5,0,-1):
#             for b in range(a):
#                 print(i,end=' ')
#             print()
#     else:
#         for a in range(1,5+1):
#             for b in range(a):
#                 print(i,end=" ")
#             print()
# 2.eliminate duplicate element
l=[1, 0, 7, 5, 9, 2, 3, 5, 7, 2, 0, 1, 10]
print(list(set(l)))
# 4.student mark
Students =[('anu',67),('amal',69),('arun',65)]
mark=[]
for i in Students:
    mark.append(i[1])
    print(mark)
    maximum=max(mark)
    print(maximum)
for j in Students:
    if j[1]==maximum:
        print(j[0])

a=input('enter num')
reverse=a[::-1]
print(reverse)
f=open('data.txt','r')
d={}
for i in f:
    s=i.rstrip('\n').split(' ')
    for i in s:
        if i not in d:
            d.update({i:1})
        else:
            value=d[i]
            value+=1
            d.update({i:value})
print(d)
div=[i for i in range(1,100+1) if i%5==0]
print(div)
