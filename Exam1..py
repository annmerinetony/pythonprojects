

#
# num=4
# for i in range(5):
#     print(i)
#     if i==num:
#         print('inside for and if')
#         break
# else:
#     print('inside else')

#
# n=int(input('enter a no.'))
# if n>1:
#     for i in range (2,n):
#       if n%i==0:
#         print(n,' is  not a prime no.')
#         break
#     else:
#        print(n,'is a prime no')
# else:
#     print(n,'not prime')

#
# n=int(input('enter a no.'))
# flag=0
# if n>1:
#     for i in range (2,n):
#       if n%i==0:
#           flag=1
#           break
#     if flag==1:
#        print('not prime')
#     else:
#        print(n,'prime')
# else:
#     print('invalid input')



# initial=int(input('enter initial no.'))
# final=int(input('enter final value'))
# for i in range(initial,final+1):
#     if i>1:
#       for j in range(2,i):
#           if i%j==0:
#               break
#       else:
#           print(i)
def prime(initial,final):
    for i in range(initial,final+1):
        if i>1:
          for j in range(2,i):
              if i%j==0:
                  break
          else:
              print(i)
prime(0,20)