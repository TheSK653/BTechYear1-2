N1=int(input())
N2=int(input())
for n in range(1,100):
    series=3*n+2
    if series%N2==0:
        continue
    print(series)
    N1-=1
    if N1==0:
        break