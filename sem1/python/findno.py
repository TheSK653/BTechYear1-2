l = [0,1]
while l[-1]<1000:
    l.append(l[-2]+l[-1])
print(l)
import re
for i in l:
    if l[-1]>1000:
        print(i,l[i])