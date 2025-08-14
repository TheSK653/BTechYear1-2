N=input()
p=N[::-1]
output=0
for i in range(len(p)):
    output+=int(p[i])*2**i
print(output)