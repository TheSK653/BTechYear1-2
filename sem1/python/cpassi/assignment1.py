p=int(input('\tEducational loan calculator\nEnter the principal loan amount (in dolars,$)\n==>$'))
r=int(input('Enter Annual interest rate (in percentage)\n==>'))/1200
n=int(input('Enter Loan term (in years)\n==>'))*12
m=(p*r*(1+r)**n)/((1+r)**n-1)
print(f'Your Monthly payment is ${m:.2f}')