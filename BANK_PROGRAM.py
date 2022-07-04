# bank balance
#
# amount=int(100000)
# withdrown=int(input('enter the amount to be withdrawn'))
# s=amount-withdrown
# print('the amount balance in your account is :', s)


amount=int(100000)
withdrown=int(input('enter the amount to be withdrawn'))
if withdrown<amount:
     s=amount-withdrown
     print('the amount balance in your account is :', s)
else:
    print('your  account balance is not sufficient')

amount=int(100000)
withdrown=int(input('enter the amount to be withdrawn'))
if withdrown>amount:
    print('insufficient balance')
else:
    s = amount - withdrown
    print('the amount balance in your account is :', s)

