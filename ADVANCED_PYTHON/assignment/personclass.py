# class Person:
#     def setperson(self,name,age):
#         self.name=name
#         self.age=age
#     def printperson(self):
#         print(self.name,self.age)
# class child:
#     def setchild(self,childno):
#         self.childno=childno
#     def printchild(self):
#         print(self.childno)
# class Student(Person):
#     college='chengal'
#     def setStudent(self,rolln,div):
#         self.rolln=rolln
#         self.div=div
#     def printstudent(self):
#         print(self.name,self.age,self.rolln,self.div,Student.college)
# class stud(Person,child):
#     def setstud(self):
#         print('multiple inh')
# class st(Student):
#     def st(self):
#         print('multilevel inhe')
# p=Student()
# p.setperson('anisha',10)
# p.setchild(3)
# p.setStudent(13,'D')
# p.printperson()
# p.pr

class book:
    def library(self,name,edition):
        self.name=name
        self.edition=edition
    def print(self):
        print(self.name,self.edition)
class book1:
    def library(self,n,e):
        self.n=n
        self.e=e
    def print(self):
        print(self.n, self.e)
e=book()
e.library('dfgg',88766)