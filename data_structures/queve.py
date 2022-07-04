queve=[]
size=int(input('enter size of queve'))
top=0
def enqueve():
    global size,top
    if top>=size:
        print('queve is full')
    else:
        e=int(input('enter element'))
        queve.append(e)
        print(queve)
        top=top+1
def dequeve():
    global top, size
    if top <= 0:
        print('queve is empty')
    else:
        # queve.remove(queve[0])
        queve.pop(0)
        top = top - 1
        print(queve)
while(True):
    opt=int(input('enter operation\n 1.enqueve\n2.dequeve'))
    if opt==1:
        enqueve()
    elif opt==2:
        dequeve()