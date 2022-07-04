# 2.

# b=[]
# for i in range(10):
#     b.append(i)
# print(b)
# b=[i for i in range(10)]
# print(b)

  # using comprehension
b=[i for i in range(1,10) if i%2==0]
print(b)

a=[1,2,3,4,55,77,23,56,98,12]
b=[i for i in a if i%2==0]
c=[i for i in a if i%2!=0]
print('even=',b)
print('odd=',c)