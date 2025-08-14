def fac(x):
    ans=x
    for i in range(2,x):
        ans*=i
    return ans

n=10
r=6
print(fac(n)/fac(r)/fac(n-r))
print(fac(n)/fac(n-r))