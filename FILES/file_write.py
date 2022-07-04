# file writing
f=open('without file name.txt','w')
f.write('attokkaran house\n kottamam')


f=open('data.txt','r')
for i in f:
    # print(i)
    s=i.rstrip('\n')
    print(s)
f=open('data2.txt','w')
f.write
