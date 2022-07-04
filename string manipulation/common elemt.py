s1="abcd"
s2="cdef"
for i in s1:
    for j in s2:
        if i==j:
            print(i)
# simple method

s1 = "abcd"
s2 = "cdef"
for i in s1:
    if i in s2:
        print(i)


