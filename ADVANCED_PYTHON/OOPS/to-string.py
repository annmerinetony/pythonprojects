# to-string
# give a value related to object
class person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printperson(self):
        print(self.name,self.age,self.place)
    def __str__(self):
        return str(self.age)+self.name
a=person('ann',23,'kalady')
print(a)
# a.printperson()
b=person('tony',59,'kottamam')
print(b)