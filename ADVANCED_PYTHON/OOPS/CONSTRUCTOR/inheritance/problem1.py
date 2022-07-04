class Person:
    def setperson(self,name,age):
        self.name=name
        self.age=age
class Parent:
    def setParent(self,place,phn):
        self.place=place
        self.phn=phn
class Employee(Person,Parent):
    def setEmployee(self,id,desig,salary):
        self.id=id
        self.desig=desig
        self.salary=salary
    def printemployee(self):
        print(self.name,self.age,self.place,self.phn,self.id,self.desig,self.salary)
a=Employee()
a.setperson('anu',38)
a.setParent('kalady',678756789)
a.setEmployee(1,'dev',66000)
a.printemployee()
