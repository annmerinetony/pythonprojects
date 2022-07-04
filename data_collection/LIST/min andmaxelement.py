a=[1,5,7,11,3,9]
a.sort()
print(a)
print('min value',a[0])
print('max value',a[-1])
a=[1,5,7,11,3,9]
new=[]
while a:
    min=a[0]
    for i in a:
        if i>min:
            min=i

