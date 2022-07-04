# 1.
space=5
for i in range(5):
    for j in range(space):
        print(end=' ')
    space-=1
    for k in range(i):
        print(i*k,end=' ')
    print()
# 2.
import re
s=input('enter string to validate')
rule='^[[A-Z]*[a-z]]\d${1}'
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print('valid')
else:
    print('invalid')

# 3.
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
    def __init__(my,name,age,place,school,rollno,dept):
        super().__init__(place,school,name,age)
        my.rollno=rollno
        my.dept=dept
    def printstudent(my):
        print(my.name,my.age,my.place,my.school,my.rollno,my.dept)
emp=student('Hazel',4,'potta','st.joseph',18,'lkg')
emp.printstudent()

# 4.
import re
s=input('enter string to validate...')
# rule='[\w._%+-]+[@][g][m][a][i][l][.][c][o][m]'
# rule='[\w._%+-]+[@][a-z]+[.][comin]+'
rule='[\w._%+-]+[@][a-z]+[.][a-z]{2,3}'
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print('valid')
else:
    print('invaild')


# 5.
def mail(func):
    def mail_check(a,b):
        if a=='abcd@gmail.com':
            return func(a,b)
        else:
            print('invalid mail id')
    return mail_check
@mail
def login(mailid,psw):
    return 'successfully completed login process'
print(login('abcd@gmail.com',5456))


# 4.gmail rule
rule='[\w._%+-]+[@][g][m][a][i][l][.][c][o][m]'
rule='[\w._%+-]+[@][a-z]+[.][comin]+'
rule='[\w._%+-]+[@][a-z]+[.][a-z]{2,3}'

