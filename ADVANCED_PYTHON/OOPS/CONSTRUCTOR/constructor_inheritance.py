class Person:
    def __init__(self,name,age,place):
        self.firstname=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.firstname)
        print(self.age)
        print(self.place)
class Student(Person):
    def __init__(self,rollno,dept,college,name,age,place):
        super().__init__(name,age,place)
        self.rollno=rollno
        self.dept=dept
        self.college=college
    def printstudent(self):
        print(self.rollno,self.dept,self.college)
a=Student(1,'eee','jyothi','ann',30,'kalady')
a.printvalue()
a.printstudent()