N=int(input('Enter no. to get its factorial\n=>'))
factorial=1
for i in range(N,0,-1):
    factorial*=i
print('\nits factorial is',factorial)