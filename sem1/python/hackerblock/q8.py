N=int(input())
if N<=1000000000 and N>2:
    prime=True
    for i in range(2,N):
        if N%i==0:
            print('Not Prime')
            prime=False
            break
    if prime==True:
        print('Prime')