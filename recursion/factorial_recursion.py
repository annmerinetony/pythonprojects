def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))

def factorial(n):
    if n==5:
        return 5
    else:
        return n*factorial(n+1)
print(factorial(1))