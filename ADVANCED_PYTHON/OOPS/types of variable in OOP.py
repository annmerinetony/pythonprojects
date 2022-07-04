# TYPES OF VARIABLE IN OOPS
# 1.instance variable    related to methords  self
# 2.static variable        related to class     class name
class student:
    college='jyothi'
    def setstudent(self,name,rollno,department):
        self.firstname=name
        self.rollno=rollno
        self.department=department
    def printvalue(self):
        print(self.firstname)
        print(self.rollno)
        print(self.department)
        print(student.college)
a=student()
a.setstudent('ann',10,'EEE')
a.printvalue()
b=student()
b.setstudent('martin',38,'CSE')
b.printvalue()
c=student()
c.setstudent('ANMY',18,'ECE')
c.printvalue()