# heterogeneous
# keep order
# duplication
#     values-allow duplication
#     keys-not allow duplication
# doesn't support indexing- call using key
# mutable
# support nesting
v={'a':1,'b':3,'c':{1:2,4:7}}
print(v)
d={'name':"ann",'age':36,'2name':"ann",'age':30}
print('name',d['name'])

d={'name':"ann",'age1':36,'2name':"ann",'age':30}
print(d)
print(type(d))
for i in d:              #i=name,age
    print(d[i])