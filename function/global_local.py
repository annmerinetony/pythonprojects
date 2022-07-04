# global and local
x=50  #local
def printx():
    global x
    x=x+100        # if we change the value of variable inside fn ,and we want it outside also, have set it as global.
    a=80
    print(x)
printx()
print(x)   # x= taken here global
print(a)   #  a not take global o/p not get

