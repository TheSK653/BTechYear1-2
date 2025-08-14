import re
n=str(input())
r=re.sub('0','5',n)
print(int(r))