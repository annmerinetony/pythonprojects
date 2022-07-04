f=open('EXAMPLE.txt','r')
# print(f)
for i in f:
    # print(i)
    s=i.rstrip('\n')
    print(s)