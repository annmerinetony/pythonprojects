class Course:
    def add_course(self,**kwargs):
        self.course_name=kwargs.get("course_name")
        self.status=kwargs.get("status")

    def __str__(self):
        return self.course_name

class Batch:
    def add_batch(self,**kwargs):
        self.course=kwargs.get("course")
        self.batch_code=kwargs.get("batch_code")
        self.start_date=kwargs.get("start_date")

    def __str__(self):
        return self.batch_code

class Student:
    def add_student(self,**kwargs):
        self.student_name=kwargs.get("student_name")
        self.email=kwargs.get("email")
        self.batch=kwargs.get("batch")
    def __str__(self):
        return self.student_name


django=Course()
django.add_course(course_name="django",status=True)
print(django)
djb1=Batch()
djb1.add_batch(course=django,batch_code="djmay2022",start_date="12-6-2022")
print(djb1.course.status)
ann=Student()
ann.add_student(student_name="ann",email="ann@gmail.com",batch=djb1)
print(ann)


ms=Course()
ms.add_course(course_name="mearn stack",status=True)
print(ms)
msb1=Batch()
msb1.add_batch(course=ms,batch_code="msapril2022",start_date="4-04-22")
martin=Student()
martin.add_student(student_name="martin",email="martin@gmail.com",batch=msb1)
print(martin)
hezek=Student()
hezek.add_student(student_name="hezek",email="martin@gmail.com",batch=msb1)
print(hezek)


bd=Course()
bd.add_course(course_name="big data",status=True)
print(bd)

students=[]
students.append(ann)
students.append(martin)
students.append(hezek)


for stud in students:
    if stud.batch.course.course_name=="mearn stack":
        print(stud.student_name)

ms_stud=[stud.student_name for stud in students if stud.batch.course.course_name=="django"]
print(ms_stud)

