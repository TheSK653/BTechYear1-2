start=int(input())
end=int(input())
f=False
count = 0
for n in range(start,end+1):
    for i in range(2,n+1):
        f=True
        if n%i==0 and not i/n==1:
            f=False
            break
    if f==True:
        print(n,end=' ')
        count+=1
print('\n',count)