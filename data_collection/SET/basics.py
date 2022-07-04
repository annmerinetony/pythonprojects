set

# 1. set is heterogenious-
#    support diff types of data(int,float,str,bool) in a single set
#    set1={1,2,3,4,5 ,10.3,True,"ann"}
# 2. set is unordered
# 3. doesn't support duplication
#    same element does not print,
#    if 1 is present true will not come,
#    if false is 0 does not come and vice versa
# 4.set is mutable
 # 5.element vice updation is not possible in set, element cannot replace with another one.
 # 6.set doesnot support indexing and slicing
 # 7.nesting not possible
a={1,2,3,{1,3,5}}
set1={1,2,3,4,5 ,10.3,False,"ann",True,1,2,3,4,5}
print(set1)
print(type(set1))
print(seti[2])
#                  empty set
set1=set()
print(set1)
print(type(set1))
set1=set()
set1.add(7)
set1.add(15.55)
set1.add(0)
set1.add(True)
set1.add(1)
set1.add("hello")
print(set1)
