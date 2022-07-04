lst=[2,3,5,7,8]
square=[]
for n in lst:
    sq=n**2
    square.append(sq)
print(square)

# MAP

def sq(n1):
    return n1**2
square=list(map(sq,lst))
print(square)

sq=list(map(lambda n:n**2,lst))
print(sq)
cube=list(map(lambda n:n**3,lst))
print(cube)

# FILTER
even=list(filter(lambda n:n%2==0,lst))
print(even)
odd=list(filter(lambda n:n%2!=0,lst))
print(odd)

op=list(map(lambda n:n-1 if n<5 else n+1,lst))
print(op)

