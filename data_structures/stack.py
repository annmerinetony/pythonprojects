# l=[]
# size= int(input('enter size of list'))
# option=int(input('1.push 2.pop'))
# for i in range(size):
#     if option==1:
#         e=int(input('enter element'))
#         l.append(e)
#         print(l)
#         if len(l)>size:
#             print('stack full')
#     else:
#         l.pop()
#         print(l)
#         if (len(l)-size)==0:
#             print('stack is empty')

stack=[]
size=int(input('enter size of stack'))
top=0
def push():
    global size,top
    if top>=size:
        print('stack is full')
    else:
        e=int(input('enter element'))
        stack.append(e)
        print(stack)
        top=top+1
def pop():
    global top,size
    if top<=0:
        print('stack is empty')
    else:
        stack.pop()
        top=top-1
        print(stack)
while(True):
    opt=int(input('enter operation\n 1.push\n2.pop'))
    if opt==1:
        push()
    elif opt==2:
        pop()

