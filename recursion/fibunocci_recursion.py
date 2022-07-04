def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
for i in range(10):
    print(fib(i))



def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
nterms=int(input('enter n terms'))
for i in range(nterms):
    print(fib(i))