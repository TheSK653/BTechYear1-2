N1,N2=int(input()),int(input())
if N1<1000000000 and N2<1000000000 and N1>0 and N2>0:
    if N1>N2:
        small=N2
    else:
        small=N1
    for i in range(2,small+1):
        if N1%i==0 and N2%i==0:
            GCD=i
    print(GCD)
