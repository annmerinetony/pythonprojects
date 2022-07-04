# class employee:
#     def setemployee(self,name,id,desig,salary,company):
#         self.name=name
#         self.id=id
#         self.desig=desig
#         self.salary=salary
#         self.company=company
#     def printvalue(self):
#         print(self.name,self.id,self.desig,self.company)
# a=employee()
# a.setemployee('ann',4565,'devol',65000,'fdhj')
# a.printvalue()
# b=employee()
# b.setemployee('anmy',5678,'team lead',75000,'infy')
# b.printvalue()


class employee:
    company="infosis"
    def setemployee(self,name,id,desig,salary):
        self.name=name
        self.id=id
        self.desig=desig
        self.salary=salary
    def printvalue(self):
        print(self.name,self.id,self.desig,employee.company)
a=employee()
a.setemployee('ann',4565,'devol',65000)
a.printvalue()
b=employee()
b.setemployee('anmy',5678,'team lead',75000)
b.printvalue()
