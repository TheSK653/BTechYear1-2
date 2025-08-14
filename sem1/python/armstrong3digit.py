a=int(input('1st '))
b=int(input('2nd '))
c=int(input('3rd '))
n1=(str(a)+str(b)+str(c))
n2=(str(a**3+b**3+c**3))
if n1==n2:
    print(n1,'is armstrong')
else:
    print(n1,'isnt armstrong as it gives',n2)