# a="my name is ann merin tony"
# s=a.split(' ')
# print(s)
# for i in s:
#     print(i)

a="my name is ann merin tony my house is at chalakudy"
s=a.split(' ')
x={}
for i in s:
    if i not in x:
        x.update({i:1})
    else:
        value=x[i]
        value+=1
        x.update({i:value})






print(x)