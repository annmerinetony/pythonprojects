# *args
def printvalue(*args):
    print(args)
printvalue(5,5.2,'hello',True)

def sum(*numbers):
    add=0
    for i in numbers:
        add+=i
    return add
print(sum(1,2,3,4,5))