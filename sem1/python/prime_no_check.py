n=int(input('enter no. =>'))
composite=True
for i in range(2,n//2+1):
    if n%i==0:
        print (n,'is not prime')
        composite=False
        break
if composite==True:
    print (n,'is prime')