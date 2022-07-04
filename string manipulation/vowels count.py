a=input ('enter the word')
x='aeiou'
count=0
for i in a:
    for j in x:
        if i==j:
            count+=1
print(count)

a=input ('enter the word')
x='aeiou'
count=0
for i in a:
        if i in x:
            count+=1
print(count)