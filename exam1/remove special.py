# f=open('specialchara.txt','r')
# v=["(!,@,#,$,%,^,&,*,(,),{,},|,_,+)"]
# n=[]
# for i in f:
#     s=i.rstrip('\n').split(' ')
#     for i in s:
#         for k in i:
#             for j in v:
#                 for l in j:
#                     n.append(k)
#     # print(n)
# n.remove(l)
# print(n)
f=open('specialchara.txt','r')
special='!@#$%^&*()_+'
b=[]
for i in f:
    s=i.rstrip('\n')
    if s.isalnum() or s.isspace() or s=="?":
        b.append(s)
    print(b)
# n=[]
# for i in f:
#     s=i.rstrip('\n').split(' ')
#     for j in special:
#         s=s.replace(i,'')
# print(s)
# import re
# string = open('specialchara.txt').read()
# new_str = re.sub('[^a-zA-Z0-9\n\.]', ' ', string)
# open('withoutchara.txt', 'w').write(new_str)

# f=open('specialchara.txt','r')
# import re
#
# string = "Hey! What's up bro?"
# new_string = re.sub(r"[^a-zA-Z0-9]","",string)
# print(new_string)
f=open('specialchara.txt','r')
special=['!@#$%^&*()_+']
for i in f:
    s=i.rstrip('\n')
    # for i in special:
    #     if i.isalnum() or i.isspace() or i == "?":
    print(s)
# f=open('data2.txt','w')
# f.write

