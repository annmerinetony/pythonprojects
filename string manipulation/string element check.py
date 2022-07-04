
 # (for single element to check 'in' can be use)
s='luminar technolab'
a=input('enter the element to be check')
if a in s:
    print('present')
else:
    print('not present')


s='luminar technolab'
a=input('enter the element to be check')
for i in s:
    if i==a:
        print('given element is present')
        break
else:
    print('given element is not present')


s='luminar technolab'
a=input('enter the element to be check')
flag=0
for i in s:
    if i==a:
        flag==1
        break
if flag==0:
    print(' present')
else:
    print('not ...present')
