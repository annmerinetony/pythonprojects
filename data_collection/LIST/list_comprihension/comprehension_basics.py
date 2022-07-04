a=[1,3,5,7]
cube=[]
for i in a:
    cube.append(i**3)
print(cube)
           # comprehension

a=[1,3,5,7]
cube=[i**3 for i in a]
print(cube)
