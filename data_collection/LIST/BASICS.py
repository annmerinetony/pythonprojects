
list=[1,2,3,4,5,1.7,'hello',0,1.7,3,True,False]
print(list)
print(type(list))
for i in list:
    print(i)
    # empty list
l=[]
print(l)
print(type(l))
             #append
l=[]
l.append(4)
l.append(4.8)
l.append("martin")
l.append(4777)
l.append(False)
print(l)
print(type(l))
#             remove
ann=[1,3,4,6,7]
ann.remove(4)        # remove one element
print(ann)
ann.pop()               # remove last element
print(ann)
ann.clear()                  # remove list
print(ann)
# del ann                           # delete entire list
print(ann)
hazel=[1,3,4,6,7]
print(hazel[3])
print(hazel[3:5])
print(len(hazel))

l=[1,3,5,6,[4,6,[4,6]]]
print(l)
l=[1,3,5,6,[4,6,[4,6]]]
print(l[4])
a=[1,3,4,6,7]
a.pop(1)
print(a)