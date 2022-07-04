# same method name,diff no of argmts
class Add1:
    def sum(self,num1,num2):
        self.num1=num1
        self.num2=num2
        print(self.num1+self.num2)
class Add2(Add1):
    def sum(self,num1,num2,num3):
        self.num1=num1
        self.num2=num2
        self.num3=num3
        print(self.num1+self.num2+self.num3)
a=Add2()
# a.sum(2,3)
a.sum(5,6,8)

# python does not support overloading