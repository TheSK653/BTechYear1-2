n=int(input('no. of line => '))
for row in range(1,n+1):
    for col in range(1,row+1):
        print('*',end=' ')
    print()

# ALT

n=int(input('no. of line => '))
for i in range(1,n+1):
    print('*'*i)