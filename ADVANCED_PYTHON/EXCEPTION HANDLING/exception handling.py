# num1=int(input('enter num1'))
# num2=int(input('enter num2'))
# print(num1/num2)

    # try -code chance to exception
    # except -what to be done after exception
    # finally
num1=int(input('enter num1'))
num2=int(input('enter num2'))
try:
    print("in try")
    print(num1/num2)
except Exception as error:
    print('zero division error',error)
finally:
    print("inside finally")
# 1. if i/p  not contain errors
#     in try
#         2.5
#     inside finally
#
# 2. if i/p contain error
# in try
# zero division error
# inside finally
