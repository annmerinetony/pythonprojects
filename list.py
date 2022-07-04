items=['apple','banana','orange']
print(items[0])
print(items[2])
print(items[0:2])
items[1]="cherry"
print(items)
print(items[-2])
#items.append=["butter"]   # WRONG

items.append("butter")     #CORRECT
print(items)
items=['apple','banana','orange']
items.insert(1,'BUTTER')
print(items)



food=['chappathi','dosa','idly']
juice=['apple','mango']
items=food+juice
print(items)
#items=food+'soda'            #wrong -string cannot be added to the list
print(items)

print(len(items))
print('chappathi' in items)
print('soda' in items)

