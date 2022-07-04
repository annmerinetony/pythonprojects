# num=input('enter a number :  ')
# num=int(num)
# if num%2==0 :
#     print('the given number is even no.')
# else:
#     print('the given number is odd no.')



#   BREAK FUNCTION


# key_location= 'chair'
# location=["garage","table","chair",'room']
# for n in location:
#     if n==key_location :
#         print("the key is found in", n)
#         break
#     else:
#         print("the key is not found in",n)
#
#  range

for i in range(1,11) :
    print(i)
for i in range(1,15):
    print(i*i)

        # CONTINUE
for i in range(1,11) :
    if i%2==0:
        continue
    else:
        print('the sqaure of ',i ,'is',i*i)






kiss= 'angry'
my_mood=['sad','happy','angry']
for n in  my_mood:
    if n==kiss:
        print('when my mood is ',n,'give kiss to your husband')
        break
    else:
        print('when my mood is ',n,'give a smile to your sweet')






