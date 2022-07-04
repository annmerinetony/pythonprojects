f1=open('data.txt','r')
v=[]
for i in f1:
    s=i.rstrip('\n').split(' ')
    v.extend(s)
print(v)