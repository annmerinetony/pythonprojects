# # remove vowels
# s=input('enter a string')
# v=('aeiou')
# for i in s:
#     if i  not in v:
#         print(i,end='')
# # 1.
# s=input('enter a string')
# v='a e i o u'
# s1=""
# for i in s:
#     if i not in v:
#         s1=s1+i
# print(s1)

# 2.
n=5
for i in range(5):
    for j in range(i,n):
        print(" ", end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()

space=8
for i in range(5):
    for j in range(space):
        print(end=" ")
    space-=2
    for k in range(i):
        print("*", end=" ")
    print()

3.
space=7
for i in range(7):
    for j in range(space):
        print(end=' ')
    space=space-1
    for k in range(i):
        print('*',end=' ')
    print()
space=2
for i in range(5,0,-1):
    for j in range(space):
        print(end=' ')
    space+=1
    for k in range(i):
        print('*',end=' ')
    print()

space=5
for i in range(5):
    for k in range(space):
        print(end=' ')
    space-=1
    for j in range(i):
        print('*',end=' ')
    print()
space=0
for i in range(5,0,-1):
    for k in range(space):
        print(end=' ')
    space+=1
    for j in range(i):
        print('*',end=' ')
    print()




# 4.
i=0
while i<5:
    print(i)
    i+=1
    if i==3:
        break
    else:
        print(0)
#5.
x=1
while True:
    if x%5==0:
        break
    print(x)
    x+=1
# 6.
n=7
c=0
while(n):
    if(n>5):
        c=c+n-1
        n=n-1
    else:
        break
print(n)
8.
for i in range(0,2,-1):
    print('hello')
    # 9.
x=0
a=3
b=4
c=5
if a>=3:
    if b>c:
        x=x+3
    elif b<c:
        x=x+5
    else:
        x=x+6
print(x)
# 10.
for i in 'luminar_technolab':
    if i=="r":
        break
    print(i)
    # 11.
x='40'
y=int(x)+2
print(y)
12.
n=[1,5,8,99,34,21,56,76,98,11,24,65,78]
prime=[]
nonprime=[]
for i in n:
    flag=0
    if i > 1:
        for j in range(2,i):
            if i%j==0:
                flag=1
                break
    if flag==1 or i==1:
        nonprime.append(i)
    else:
        prime.append(i)
print('prime numbers',prime)
print('non prime numbers', nonprime)
n=[1,5,8,99,34,21,56,76,98,11,24,65,78]
prime=[]
nonprime=[]
for i in n:
    if i > 1:
        for j in range(2,i):
            if i%j==0:
                nonprime.append(i)
                break
        else:
            prime.append(i)
    elif i==1:
        nonprime.append(i)

print('prime numbers',prime)
print('non prime numbers', nonprime)
13.

str='hell@#o ho%^&w are y*&(ou?'
b=""
for i in str:
    if i.isalnum() or i.isspace() or i=="?":
        b+=i
print(b)

# str="Fo%r most Unix systems, you must download and compilethe {source code. ]The same@ source code archive canalso! be ^used to? build the> Windows and Mac vers)ions,and is the starting point for$ ports< to all oth?er platforms"
# special = '!@#$%^&*()_+{}|[]<>'
# for i in special:
#     str=str.replace(i,'')
# print(str)
# str="Fo%r most Unix systems, you must download and compile the {source code. ]" \
#     "The same@ source code archive canal so! be ^used to? build the> Windows and Mac vers)ions," \
#     "and is the starting point for$ ports< to all oth?er platforms"
# special = '!@#$%^&*()_+{}[]:";<>?/'
# for i in special:
#     str=str.replace(i,'')
# print(str)


# f=open('specialchara.txt','r')
# for i in f:
#     str = i.rstrip('\n')
# special = '!@#$%^&*()_+{}|[]<>'
# for i in special:
#     str = str.replace(i,'')
# print(str)
f=open('specialchara.txt','r')
for i in f:
    str = i.rstrip('\n')
special = '!@#$%^&*()_+{}|[]<>"?,.'
n=""
for j in str:
    if j not in special:
        n=n+j
print(n)
f=open('specialchara.txt','r')
for i in f:
    str = i.rstrip('\n')
special="QWERTYUIOPASDFGHJKLZXCVBNM qwertyuiopasdfghjklzxcvbnm"
n=""
for j in str:
    if j in special:
        n=n+j
print(n)


