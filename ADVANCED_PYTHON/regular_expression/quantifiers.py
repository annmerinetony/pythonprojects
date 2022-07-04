# quantifiers
import re
count=0
rule='a$'
matcher=re.finditer(rule,'aaa abcaa@123')
for i in matcher:
    print(i.start())
    print(i.group())
    count=count+1
print(count)