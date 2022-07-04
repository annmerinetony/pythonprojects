# regular expression
# re pattern matching
# finditer fullmatch
#
# import re
# count=0
# s='abaaaaabbbbab'
# matcher=re.finditer('ab',s)
# for i in matcher:
#     print(i.group())
#     print(i.start())
#     count=count+1
# print(count)

import re
count=0
rule='[^abc]'
matcher=re.finditer(rule,'abcd@123')
for i in matcher:
    print(i.start())
    print(i.group())
    count=count+1
print(count)