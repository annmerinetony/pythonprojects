# single inheritance
class Person:
    def setperson(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printperson(self):
        print(self.name,self.age,self.place)
class Student(Person):
    college='chengal'
    def setStudent(self,rolln,div):
        self.rolln=rolln
        self.div=div
    def printstudent(self):
        print(self.name,self.age,self.place,self.rolln,self.div,Student.college)
p=Student()
p.setperson('anisha',10,'kottamam')
p.setStudent(13,'D')
p.printperson()