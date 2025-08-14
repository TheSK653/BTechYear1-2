N=int(input())
n=len(str(N))
sum=0
temp=N
while temp>0:
    digit=temp%10
    sum+=digit**n
    temp//=10
if N==sum:
    print('true')
else:
    print('false')