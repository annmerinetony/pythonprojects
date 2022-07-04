size=int(input("enter size"))
even=[]
odd=[]
for i in range(size):
    e=int(input('enter element'))
    if e%2==0:
        even.append(e)
    else:
        odd.append(e)
print('even list=',even)
print('odd list=',odd)