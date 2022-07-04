import re
rule='[P][Y]\d{2}'
s=open('regnum.txt','r')
x=open('python.txt','w')
for i in s:
    d=i.rstrip('\n')
    matcher=re.fullmatch(rule,d)
    if matcher is not None:
        x.write(d)
        x.write('\n')
