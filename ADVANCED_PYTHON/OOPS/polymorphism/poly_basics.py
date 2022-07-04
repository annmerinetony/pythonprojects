# polymorphism -manyforms -different duplicates
# 1.method overloading
# 2.method overriding

class A:
    def printa(self):
        print('inside a')
class B:
    def printa(self):
        print('inside b')

        # same method(printa) diff class is not a problem

class A:
    def printa(self):
        print('inside a')

class B(A):
    def printa(self):
        print('inside b')
        # but if we inherit class ,we can't use same method