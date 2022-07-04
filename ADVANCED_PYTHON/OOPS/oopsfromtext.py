# class Person:
#     def __init__(self,name,age,place):
#         self.name=name
#         self.age=age
#         self.place=place
#     def printperson(self):
#         print(self.name,self.age,self.place)
#         print('..............')
# a=open('oops.txt','r')
# for i in a:
#     s=i.rstrip('\n').split(',')
#     name=s[0]
#     age=s[1]
#     place=s[2]
#     x=Person(name,age,place)
#     x.printperson()


class Student:
    def __init__(self,name,rollno,dept,mark):
        self.name=name
        self.rollno=rollno
        self.dept=dept
        self.mark=mark
    def printstudent(self):
        print(self.name)
        print(self.rollno)
        print(self.dept)
        print(self.mark)
        print('+++++++++++')
f=open('student.txt','r')
l=[]
for i in f:
    s=i.rstrip('\n').split(',')
    name=s[0]
    rollno=s[1]
    dept=s[2]
    mark=s[3]
    z=Student(name,rollno,dept,mark)
    # z.printstudent()
    print(z.name)
    l.append(rollno)
print(l)

