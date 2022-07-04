# 3.
even=lambda n:n%2==0
print(even(2))
class animal:
    def __init__(self,type,food):
        self.type=type
        self.food=food
class dog(animal):
    def __init__(self,name,age,type,food):
        super().__init__(type,food)
        self.name=name
        self.age=age
    def printdog(self):
        print(self.type,self.food,self.name,self.age)
a=dog('dog','meals&meat','jakie',2)
a.printdog()

# import re
# s=input('enter string to validate')
# rule='[a]\d{5}[b]'
# matcher=re.fullmatch(rule,s)
# if matcher is not None:
#     print('valid')
# else:
#     print('invaild')
#
# import re
# s=input('enter string to validate')
# rule='[A-Z][\W[a-z]'
# matcher=re.fullmatch(rule,s)
# if matcher is not None:
#     print('valid')
# else:
#     print('invaild')

# n1=int(input('enter n1'))
# n2=int(input('enter n2'))
# try:
#     print(n1/n2)
# except:
#     print('zero division error')
# # finally:
# #     print('give output always')
#
# # import re
# # s=input('enter string to validate')
# # rule='[A-Z][\d\w]{3,8}[A-Z]'
# # matcher=re.fullmatch(rule,s)
# # if matcher is not None:
# #     print('valid')
# # else:
# #     print('invaild')
# import re
# rule='[+][9][1]\d{10}'
# s=open('phoneno.txt','r')
# for i in s:
#     d=i.rstrip('\n').split(' ')
#     for j in d:
#         matcher=re.fullmatch(rule,j)
#         if matcher is not None:
#             print(j,'is valid phone number')
#         else:
#             print(j,'is invalid phone number')
#
# import re
# s=input('enter string to validate')
# rule='[+][9][1]\d{10}'
# matcher=re.fullmatch(rule,s)
# if matcher is not None:
#     print('valid')
# else:
#     print('invaild')
#
class student:
    def __init__(self,name,rollno,dep,mark):
        self.name=name
        self.rollno=rollno
        self.dep=dep
        self.mark=mark
    def printvalue(self):
        print(self.name,self.rollno,self.dep,self.mark)
s=open('studentmaxmark.txt','r')
for i in s:
    d=i.rstrip('\n').split(' ')
    print(d)
class vehicle:
    def __init__(self,name,no):
        self.name=name
        self.no=no
    def print(self):
        print(self.name,self.no)
class bus(vehicle):
    def __init__(self,owner,licence,name,no):
        super().__init__(name,no)
        self.owner=owner
        self.licence=licence
    def print(self):
        print(self.owner,self.licence,self.name,self.no)

x=bus('tony',345677,'yathra',87)
x.print()
