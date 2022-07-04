d={'name':'ann','age':30,'place':'kalady','post':'potta'}
e=input('enter key')
# methord 1
# for i in d:
#     if i==e:
#         print('present')
#         break
# else:
#         print('not present')

# methord2
print(d.keys())
if e in d.keys():
    print('present')
else:
    print('not present')

