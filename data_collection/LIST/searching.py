a=[5,2,88,35,23,9,100,34,33]
e=int(input('enter element'))
flag=0
a.sort()
lower=0
upper=len(a)-1
while lower<=upper:
    mid=(lower+upper)//2
    if a[mid]==e:
        flag=1
        break
    elif e<a[mid]:
        upper=mid-1
    elif e>a[mid]:
        lower=mid+1
if flag==1:
    print('present')
else:
    print('not present')