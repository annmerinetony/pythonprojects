class student:
    def __init__(self,name,rollno,dep,mark):
        self.name=name
        self.rollno=rollno
        self.dep=dep
        self.mark=mark
    def printvalue(self):
        print(self.name,self.rollno,self.dep,self.mark)
    # def __str__(self):
    #     return str(self.mark)

s=open('studentmaxmark.txt','r')
l=[]
for i in s:
    d=i.rstrip('\n').split(' ')
    print(d)

    for j in d:
        u = d.split(',')
        name=j[0]
        rollno=j[1]
        dep=j[2]
        mark=j[3]
        x=student(name,rollno,dep,mark)
        print(x.mark)


    # for j in d:
    #     # for k in j:
    #     print(j)
    #     j.sort()
    #     print(j)