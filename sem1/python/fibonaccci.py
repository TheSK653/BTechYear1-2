limit=int(input('Enter limit => '))
num1,num2,num3=0,1,0
print(num1,end=', ')
print(num2,end=', ')
for i in range(3,limit+1):
    num3=num1+num2
    print(num3,end=', ')
    num1,num2=num2,num3