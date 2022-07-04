# import re
# s=input('enter string to validate')
# rule='[a][\w\W]*[b]'
# matcher=re.fullmatch(rule,s)
# if matcher is not None:
#     print('valid')
# else:
#     print('invaild')
import re
s=input('enter string to validate')
rule='[a-zA-Z][\w\W]{8}[0-9]'
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print('valid')
else:
    print('invaild')

# import re
# s=input('enter string to validate')
# rule='\D{5}'
# matcher=re.fullmatch(rule,s)
# if matcher is not None:
#     print('valid')
# else:
#     print('invaild')
import re
s=input('enter string to validate')
rule='[\w._%+-]+[g][m][a][i][l][.][c][o][m]'
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print('valid')
else:
    print('invaild')
# import re
# s=input('enter string to validate')
# rule='\d[\w\W]{3}\d'
# matcher=re.fullmatch(rule,s)
# if matcher is not None:
#     print('valid')
# else:
#     print('invaild')
# import re
# s=input('enter string to validate')
# rule='[a-z][\W\w]{3,8}[A-Z]'
# matcher=re.fullmatch(rule,s)
# if matcher is not None:
#     print('valid')
# else:
#     print('invaild')

import re
s=input('enter string to validate')
rule='\d{4}\W[a-z]{1}'
matcher=re.fullmatch(rule,s)
if matcher is not None:
    print('valid')
else:
    print('invaild')
