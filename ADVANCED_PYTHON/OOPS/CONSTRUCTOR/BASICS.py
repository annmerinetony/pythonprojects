# INITIALIZE INSTANCE VARIABLE WHEN OBJECT CREATION
class person:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def printperson(self):
        print(self.name,self.age,self.place)
a=person('ann',23,'kalady')
a.printperson()

class nurse:
    hospital='l.f'
    def __init__(self,name,age,dep):
        self.name=name
        self.age=age
        self.dep=dep
    def printnurse(self):
        print(self.name,self.age,self.dep,nurse.hospital)
x=nurse('anisha',25,'paediatric')
x.printnurse()
y=nurse('jismy',35,'psyciatric')
y.printnurse()