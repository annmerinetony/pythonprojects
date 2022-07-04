class student:
    def setstudent(self,name,rollno,department,college):
        self.firstname=name
        self.rollno=rollno
        self.department=department
        self.college=college
    def printvalue(self):
        print(self.firstname)
        print(self.rollno)
        print(self.department)
        print(self.college)
a=student()
a.setstudent('ann',10,'EEE','JYOTHI')
a.printvalue()
b=student()
b.setstudent('martin',38,'CSE','GOVT.POLYTECHNIC')
b.printvalue()
c=student()
c.setstudent('ANMY',18,'ECE','RAJAGIRI')
c.printvalue()
