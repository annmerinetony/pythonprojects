# num1=2
# num2=5
# num3=-9
# if num1>0 and num2==0 and num3<0:
#     print('hello')
# if num1>0 or num2==0 or num3<0:
#     print('hello')

score=int(input('enter total score'))
if score<=100:
    if score>=90:
        print('your grade is  : A+')
    elif score>=80:
        print('your grade is  : A')
    elif score >= 70:
        print('your grade is  : B+')
    elif score>=60:
        print('your grade is  : B')
    else:
        print ('you are failed')
else:
    print('invalid input')
