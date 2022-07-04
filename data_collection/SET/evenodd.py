A={1,2,3,4,5,6,7,8,9}
even=set()
odd=set()
for i in A:
    if i%2==0:
        even.add(i)
    else:
        odd.add(i)
print(even)
print(odd)