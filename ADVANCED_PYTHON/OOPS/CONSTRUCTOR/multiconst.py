class person:
    def __init__(my,name,age):
        my.name=name
        my.age=age
class parent:
    def __init__(my,place,phn):
        my.place=place
        my.phn=phn
class employee(person,parent):
    def __init__(my,id,desig,salary,name,age,place,phn):
        person.__init__(my,name,age)
        parent.__init__(my,place,phn)
        my.id=id
        my.desig=desig
        my.salary=salary
    def printemployee(my):
        print(my.name,my.age,my.place,my.phn,my.id,my.desig,my.salary)
emp=employee(1,'dev',55000,'alwin',44,'aluva',956656)
emp.printemployee()
