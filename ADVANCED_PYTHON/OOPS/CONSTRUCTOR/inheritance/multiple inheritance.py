# multiple inheritance
# more than one parent
class A:
    def printa(self):
        print('inside a')
class B:
    def printb(self):
        print('inside b')
class C(A,B):
    def printc(self):
        print('inside c')
x=C()
x.printb()
x.printa()
x.printc()