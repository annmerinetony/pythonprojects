# f=open('specialchara.txt','r')
# b=''
# for i in f:
#     s=i.rstrip('\n')
#     print(s)
#     special = '!@#$%^&*()_+'
#     for j in special:
#         if i.isalnum() or i.isspace() or i == "?":
#             b+=i
#             print(s)
#
# str="Fo%r most Unix systems, you must download and compile the {source code. ]" \
#     "The same@ source code archive canal so! be ^used to? build the> Windows and Mac vers)ions," \
#     "and is the starting point for$ ports< to all oth?er platforms"
# special = '!@#$%^&*()_+{}[]:";<>?/'
# for i in special:
#     str=str.replace(i,'')
# print(str)


f=open('specialchara.txt','r')
for i in f:
    str = i.rstrip('\n')
special = '!@#$%^&*()_+{}|[]<>'
for i in special:
    str = str.replace(i,'')
print(str)
