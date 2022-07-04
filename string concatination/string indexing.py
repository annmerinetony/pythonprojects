# # +ve indexing 01234...
# # -ve indexing -1,-2,-3,...
# s="luminar technolab"
# print(s[0])
# print(s[4])
# print(s[-5])
# print(s[7])
# print(s[-3])
# print(s[21])

def s():
    s = input("enter a word")
    print("the first letter of ",s,"is",s[0])
s()

def firstletter(s):
    return s[0]
print(firstletter("hello"))
print(firstletter("ann"))

def firstletter(s):
    print(s[0])
firstletter("sdghjy")
firstletter("hjghn")