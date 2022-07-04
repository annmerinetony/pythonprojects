# overriding
# same method name same no of argmts
class Add:
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print('inside parent',self.num1+self.num2)
class Add2():
    def sum(self,no1,no2):
        self.no1=no1
        self.no2=no2
        print('inside child',self.no1+self.no2)
a=Add2()
a.sum(4,2)
        # o/p of latest child will get

# class Parent:
#     def setparent(self,name,age):
#         self.name=name
#         self.age=age
#         print(self.name,self.age)
# class Student(Parent):
#     def setparent(self,roll,div):
#         self.roll=roll
#         self.div=div
#         print(self.roll,self.div)
# a=Student()
# a.setparent(11,'d')
# a.setparent('cdgh',9)

class A:
    def printdata(self):
        print('method 1')
    def pri
