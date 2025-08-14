entries=input().split()
a,b,c=int(entries[0]),int(entries[1]),int(entries[2])
D=int(b**2-4*a*c)
if D>=0:
    root1=int((-b-D**(1/2))/(2*a))
    root2=int((-b+D**(1/2))/(2*a))
    if D!=0:
        print('Real and Distinct')
    else:
        print('Real and Equal')
    print(root1,root2)
else:
    print('Imaginary')