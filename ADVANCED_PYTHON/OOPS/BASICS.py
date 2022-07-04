# Object oriented programming
# class design
# object realworld entity
# reference

# self...instance keyword
#      we can use variable to all methords
class person:
    def reading(self):
        print('reading books')
    def writing(self):
        print('person writing')
a=person()   #object1
a.reading()
a.writing()
b=person()    #object2
b.writing()
b.reading()

class person:
    def setvalue(self,name,age,place):
        self.firstname=name
        self.age=age
        self.place=place
    def printvalue(self):
        print(self.firstname)
        print(self.age)
        print(self.place)
a=person()
a.setvalue('ann',30,'chalakudy')
a.printvalue()
b=person()
b.setvalue('martin',38,'potta')
b.printvalue()

