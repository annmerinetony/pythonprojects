# multilevel/hierarchial
class A:
    def seta(self):
        print('inside a')
class B(A):
    def setb(self):
        print('inside b')
class C(B):
    def setc(self):
        print('inside c')
x=C()
x.seta()
x.setc()
x.setb()
y=B()
y.seta()
y.setb()

class Person:
    school='St.Joseph School,Aloor'
    def setperson(self,name,age):
        self.name=name
        self.age=age
class Child(Person):
    def setchild(self,place,phn):
        self.place=place
        self.phn=phn
    def printchild(self):
        print(self.name,self.age,self.place,self.phn)
class Student(Child):
    def setStudent(self,rolln,div):
        self.rolln=rolln
        self.div=div
    def printStudent(self):
        print(self.name,self.age,self.place,self.phn,self.rolln,self.div,Person.school)
x=Student()
x.setperson('hazel',4)
x.setchild('chalakudy',7845545535)
x.setStudent(15,'lkg')
x.printStudent()

y=Child()
y.setchild('kalady',5453232)
y.setperson('hezek',1)
y.printchild()



