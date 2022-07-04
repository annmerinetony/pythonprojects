# amount=int(input('enter the amount to be withdrown'))
# if(amount>2000):
#     n=amount//2000
#     a = (n * 2000)
#     c = ((amount - a)// 500)
#     b=amount-a-500*c
#     b!=0
#     b1 = b//100
#
#     print('the no.of 2000 note to given',n)
#     print('the no.of 500 note to given',c)
#     print('the no.of 100 note to given', b1)
# else:
#     q=(amount//500)
#     print('the no.of 500 note to given', q)
#     r=(amount-500*q)//100
#     print('the no.of 100 note to given', r)

amount=int(input('enter the amount to be withdrown'))
if(amount>2000):
    n=amount//2000
    a = (n * 2000)
    c = ((amount - a)// 500)
    b=amount-a-500*c
    b!=0
    b1 = b//100
      if (amount - (2000 * n - 500 * c - 100 * b1)) != 0:
        print('in valid withdrawal')
      else:
        print('the no.of 2000 note to given', n)
        print('the no.of 500 note to given', c)
        print('the no.of 100 note to given', b1)

else:
    q=(amount//500)
    r = (amount - 500 * q) // 100
    if (amount-(500*q-100*r))==0:
        print('the no.of 500 note to given', q)
        print('the no.of 100 note to given', r)
    else:
        print('in valid withdrawal')



