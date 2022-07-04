set1={2,-4,6,8,-11,-55,-76,65,45,-100}
posi=set()
nega=set()
for i in set1:
    if i>0:
        posi.add(i)
    else:
        nega.add(i)
print("positive set =",posi,"\nnegative set =",nega)


