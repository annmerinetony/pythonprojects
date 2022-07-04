# # swapping of numbers
#
# num1=int(input('enter num1 = '))
# num2=int(input('enter num2 = '))
# print('the swap no. of ' ,num1,'is',num2)
# print('the swap no. of ',num2, 'is',num1)
#
#
# a=int(input('enter a = '))
# b=int(input('enter b = '))
# a,b=b,a
# print( 'swap no.',b ,'=',a)
# print( 'swap no. ',a ,'=',b)

#
# num1=int(input('enter num1'))
# num2=int(input('enter num2'))
# print('before swapping num1=',num1)
# print('before swapping num2=',num2)
# temp=num1
# num1=num2
# num2=temp
# print('after swapping num1=',num1)
# print('after swapping num2=',num2)



num1=int(input('enter num1'))
num2=int(input('enter num2'))
print('before swapping num1=',num1)
print('before swapping num2=',num2)
num1=num1+num2
num2=num1-num2
num1=num1-num2
print('after swapping num1=',num1)
print('after swapping num2=',num2)