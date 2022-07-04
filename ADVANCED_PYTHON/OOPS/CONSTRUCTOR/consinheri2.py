class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printvalue1(self):
        print(self.name,self.age)
class B(A):
    def __init__(self,husname,childno,name,age):
        super().__init__(name,age)
        self.husname=husname
        self.childno=childno
    def printvalue2(self):
        print(self.husname,self.childno)
a=B('martin',2,'merin',30)
a.printvalue1()
a.printvalue2()

