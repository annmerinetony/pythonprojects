# # print(4+3%5)
# temp = ['Geeks', 'for', 'Geeks']
#
# # arr = [i[0].upper() for i in temp]
# # print(arr)

# # 11.
# n=input('enter a name')
# s=n.split(' ')
# print(s[-1],s[1],s[0])
#
# # 12.
# n=input('enter a string')
# s=n[-2]+n[-1]+n[0]+n[1]
# print(s)









def check(s1,s2):
    if (sorted(s1) == sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagram.")
s1 = "listen"
s2 = "silent"
check(s1,s2)


def find(n):
   if (n == 0):
      return False
   while (n != 1):
      if (n % 2 != 0):
         return False
      n = n // 2
   return True
print(find(98))

def find(n):
   if (n == 0):
      return ('not power of 2')
   while (n != 1):
      if (n % 2 != 0):
         return ('not power of 2')
      n = n // 2
   return ('power of 2')
print(find(8))








class add:
   def __init__(self,num1,num2):
      self.num1=num1
      self.num2=num2
   def printadd(self):
      print(self.num1+self.num2)
s=add(2,3)
s.printadd()


class Demo:
   x = 20  # Public
   _y = 30  # Protected
   __z = 40  # Private
   a = __z
d = Demo()
print(d.x)
print(d._y)
print(d.a)


# import re
# s=input('enter string to validate')
# rule='[[A-Z]*[a-z]][\W\w]{8}\d{1}'
# matcher=re.fullmatch(rule,s)
# if matcher is not None:
#     print('valid')
# else:
#     print('invalid')

# import re
# s=input('enter string to validate')
# rule='\d*[\w\W]+[A-Z]'
# matcher=re.fullmatch(rule,s)
# if matcher is not None:
#     print('valid')
# else:
#     print('invalid')