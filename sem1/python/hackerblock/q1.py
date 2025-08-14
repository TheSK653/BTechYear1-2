N=str(input())
limit=(len(N)*-1)-1
sum_odd=0
sum_even=0
for i in range(-1,limit,-2):
    sum_odd+=int(N[i])
print(sum_odd)
for i in range(-2,limit,-2):
    sum_even+=int(N[i])
print(sum_even)