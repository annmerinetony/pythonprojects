# def add(num1,num2):
#     print(num1+num2)
# def sub(num1,num2):
#     print(num1 - num2)
# def mul(num1,num2):
#     print(num1 * num2)
# def div(num1,num2):
#     print(num1 / num2)
# while True:
#     option=int(input('select option\n 1.additon\n 2.substraction\n 3.multiplication\n 4.divition\n 5.stop'))
#     if option>=5:
#         print('invalid')
#         break
#     else:
#         num1=float(input('enter num1'))
#         num2=float(input('enter num2'))
#         if option==1:
#             add(num1, num2)
#         elif option==2:
#             sub(num1, num2)
#         elif option==3:
#             mul(num1, num2)
#         elif option==4:
#             div(num1, num2)



def add(num1,num2):
    print(num1+num2)
def sub(num1,num2):
    print(num1 - num2)
def mul(num1,num2):
    print(num1 * num2)
def div(num1,num2):
    print(num1 / num2)
while True:
    option=input('select option\n 1.additon\n 2.substraction\n 3.multiplication\n 4.divition\n 5.stop')
    if option=='5':
        break
    elif option in "1234":
        num1=float(input('enter num1'))
        num2=float(input('enter num2'))
        if option=='1':
            add(num1, num2)
        elif option=='2':
            sub(num1, num2)
        elif option=='3':
            mul(num1, num2)
        elif option=='4':
            div(num1, num2)
    else:
        print('invalid')


#
# def add(num1,num2):
#     print(num1+num2)
# def sub(num1,num2):
#     print(num1 - num2)
# def mul(num1,num2):
#     print(num1 * num2)
# def div(num1,num2):
#     print(num1 / num2)
# while True:
#     option=int(input('select option\n 1.additon\n 2.substraction\n 3.multiplication\n 4.divition\n 5.stop'))
#     if option<=4 or option<5:
#         num1=float(input('enter num1'))
#         num2=float(input('enter num2'))
#         if option==1:
#             add(num1, num2)
#         elif option==2:
#             sub(num1, num2)
#         elif option==3:
#             mul(num1, num2)
#         elif option==4:
#             div(num1, num2)
#     elif option>5:
#             print('invalid')
#
