def sum(n):
    sum=0
    for i in range (-5,11):
      if i>0:
        sum+=i
    print(sum)
sum(10)

def sum(n1,n2):
    sum=0
    for i in range (n1,n2+1):
      if i>0:
        sum+=i
    print(sum)
sum(-5,10)


def grade(n):
    if n<100:
        if n>90:
            return ('A+')
        elif n>80:
            return ('A')
        elif n>70:
            return ('B+')
        elif n>60:
            return ('B')
        else:
            return("fail")
    else:
        return ("invalid")
n = int(input('enter mark'))
print(grade(n))

def grade(n):
    if n<100:
        if n>90:
            return ('A+')
        elif n>80:
            return ('A')
        elif n>70:
            return ('B+')
        elif n>60:
            return ('B')
        else:
            return("fail")
    else:
        return ("invalid")
print(grade(79))

#
#
def sum(n1,n2):
    sum=0
    for i in range(n1,n2+1):
        if i%2!=0:
            sum = sum+i
    print(sum)
sum(20,30)
def sum():
    sum=0
    for i in range(20,31):
        if i%2!=0:
            sum = sum+i
    print(sum)
sum()


def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
n=int(input('enter number'))
fact(n)