f1=open('data.txt','r')
f2=open('data2.txt','w')
for i in f1:
    s=i.rstrip('\n')
    f2.write(s)
    f2.write('\n')

