class A:      #parentclass/
    def printa(self,num):
        self.num=num
        print('inside A class',self.num)
class B(A):     #child class/sub class/derived class
    def printb(self,num1):
        self.num1=num1
        print('inside class B',self.num1,self.num)

b=B()
b.printa(10)
b.printb(8)