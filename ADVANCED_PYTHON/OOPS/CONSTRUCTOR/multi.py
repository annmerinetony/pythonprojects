class person:
    def __init__(my,name,age):
        my.name=name
        my.age=age
class child(person):
    def __init__(my,place,school,name,age):
        super().__init__(name,age)
        my.place=place
        my.school=school
class student(child):
    def __init__(my,rollno,dept,place,school,name,age):
        super().__init__(place,school,name,age)
        my.rollno=rollno
        my.dept=dept
    def printstudent(my):
        print(my.name,my.age,my.place,my.school,my.rollno,my.dept)
emp=student('anmt',27,'kaldy','infy',344567,'ec')
emp.printstudent()