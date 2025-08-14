#Take N as input. Print Nth Fibonacci Number, given that the first two numbers in the Fibonacci Series are 0 and 1.
N=int(input())
num1,num2,num3=0,1,0
for i in range(2,N+1):
    num3=num1+num2
    num1,num2=num2,num3
print(num3)