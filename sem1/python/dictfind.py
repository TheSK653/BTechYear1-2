import re
list={0:0}
i=1
list[i]=1
while i<19:
    i+=1
    list[i]=list[i-1]+list[i-2]
for k,v in list.items():
    if re.findall(r'\d*',v)>1000:
        print ('before this')