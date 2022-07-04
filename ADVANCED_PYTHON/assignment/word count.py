f=open('data2.txt','r')
d={}
for i in f:
    # u=i.upper()
    l=i.lower()
    s=l.rstrip('\n').split(' ')
    for i in s:
        if i not in d:
            d.update({i:1})
        else:
            value=d[i]
            value+=1
            d.update({i:value})
print(d)
class person:
    def __init__(self,name,id,desi,salary):
        self.name=name
        self.id=id
        self.desi=desi
        self.salary=salary
    def printvalues(self):
        print(self.name,self.id,self.desi,self.salary)
f=open('empoly details','r')
for i in f:
    s=i.rstrip('\n')
    print(s)
class pet:
    def __init__(self,animal,owner):
        self.animal=animal
        self.owner=owner
class cat(pet):
    def __init__(self,name,age,animal,owner):
        super().__init__(animal,owner)
        self.name=name
        self.age=age
    def printcat(self):
        print(self.name,self.age,self.animal,self.owner)
s=cat('julie',2,'cat','Mr.Martin')
s.printcat()

# def sum_odd(num1,num2):
#     sum=0
#     for i in range(40,80):
#         if i%2!=0:
#             print(i)
#         sum+=i
#     return sum
# print(sum_odd(40,80))
