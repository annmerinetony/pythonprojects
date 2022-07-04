#
#     # first recursive
#
# s=input('enter a word')
# a=""
# for i in s:
#     if i not in a:
#         a=a+i
#     else:
#         print('first recursive letter',i)
#         break
#
#
#         # last recursive
# s=input('enter a word')
# a=""
# n=""
# for i in s:
#     if i not in a:
#         a=a+i
#     else:
#         n=n+i
# print('last recursive letter',n[-1])
# print('first recursive letter',n[0])

s=input('enter a word')   #aaabbbc
a=""
n=""
for i in s:          #a,a,a,b,b,b,c
    if i not in a:   #a,b,c
        a=a+i
    else:
        if i not in n:  #a,b
            n=n+i

print(n)
print('last recursive letter',n[-1])
print('first recursive letter',n[0])
print('second recursive',n[1])
