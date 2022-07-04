# # decorators
# def changevalue(func):
#     def wrapper(a,b):
#         if a<b:
#             a,b=b,a
#             return func(a,b)
#         else:
#             return func(a,b)
#     return wrapper
# @changevalue
# def sub(n1,n2):
#     return n1-n2
# print(sub(5,10))
# @changevalue
# def div(n1,n2):
#     return n1/n2
# print(div(2,5))
def dec_fun(fn):
    def inner_fun(n1,n2):
        if n2>n1:
            (n1,n2)=(n2,n1)
        return fn(n1,n2)
    return inner_fun

@dec_fun
def sub(n1,n2):
    return n1-n2
@dec_fun
def div(n1,n2):
    return n1/n2

print(sub(10,20))
print(div(10,20))
# def value(func):
#     def wr(a,b):
#         if a<b:
#             a,b=b,a
#             return func(a,b)
#         else:
#             return func(a,b)
#     return wr
# @value
# def sub(n1,n2):
#     return n1-n2
# print(sub(5,10))
#
