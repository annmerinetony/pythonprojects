# recursion
# function call itself
# factorial
#
#
# def fact(n):
#     fact = 1
#     for i in range(1,6):
#         fact=fact*i
#     print(fact)
# fact(5)
#
# # recursion
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

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)