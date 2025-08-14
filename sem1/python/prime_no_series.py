# n=int(input('enter no. =>'))
# count=0
# if count<n:
#     for i in range(2,):
        
n=int(input('Number of prime no. to print\n=>'))
for i in range(2,100):
    flag=True
    for j in range(2,i):
        if i%j==0:
            flag=False
            break
    if flag==True:
        print(i)
        n-=1
    if n==0:
        break