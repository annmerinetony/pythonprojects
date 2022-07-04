# w=input('enter a word')
# new_string=""
# for i in w:
#     if i not in "aeiou":
#         new_string=new_string+i
# print(new_string)

w=input('enter a word')
n=input("enter remove")
e=""
for i in w:
    if i not in n:
        e=e+i
print(e)
