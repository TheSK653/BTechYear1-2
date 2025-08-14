i=[]
s=0
while True:
    i.append(int(input()))
    s+=i[-1]
    if s==0:
        break
print(sum([x**2 for x in i]))