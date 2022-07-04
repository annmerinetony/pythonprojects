# # def fibunocci():
# # #     n=int(input('enter number'))
# # #     a=0
# # #     b=1
# # #     print(a)
# # #     print(b)                                        # if n=10 but 11 o/p will get
# # #     for i in range(2,n):
# # #         c=a+b
# # #         a=b
# # #         b=c
# # #         print(c)
# # # fibunocci()
# #
# # def fibunocci():
# #     n=int(input('enter number'))
# #     if n > 0:
# #         a=0
# #         b=1
# #         if n==1:
# #             print(a)
# #         else:
# #             print(a)
# #             print(b)
# #             for i in range(2,n):
# #                 c=a+b
# #                 a=b
# #                 b=c
# #                 print(c)
# # fibunocci()
# def fib(n):
#     if n > 0:
#             a=0
#             b=1
#             if n==1:
#                 print(a)
#             else:
#                 print(a)
#                 print(b)
#                 for i in range(2,n):
#                     c=a+b
#                     a=b
#                     b=c
#                     print(c)
# n=int(input('enter number'))
# fib(n)

   # for
n=int(input('enter the number'))
a=0
b=1
for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c


    # while
n=int(input('enter the number'))
a=0
b=1
i=0
while i<n:
    print(a)
    c = a + b
    a = b
    b = c
    i=i+1

