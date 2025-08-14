l=list(map(int,input().split()))
temp=l[-1]
for i in range(1,len(l)):
    l[-i]=l[-i-1]
l[0]=temp
print(l)