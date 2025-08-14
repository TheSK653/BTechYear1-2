#it print the mention seriess of number with the given interval
start=int(input('starting no.='))
end=int(input('ending no.='))
evensum=0
oddsum=0
s1=[]
s2=[]
for i in range(start,end+1):
    if i%2==0:
        evensum+=i
        s1.append(i)
    else:
        oddsum+=i
        s2.append(i)
print(f'Sum of even no. = {evensum}')
print(f'Sum of odd no. = {oddsum}')
print('even no.s',s1)
print('even no.s',s2)