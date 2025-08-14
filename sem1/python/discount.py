purchase_amount=float(input('Enter purchase amount of your items \n=> $ '))
ans=input('Are you an member?(yes/no)\n')
if purchase_amount>=100 and (ans=='Yes'or ans=='yes' or ans=='Y' or ans=='y'):
    payble=purchase_amount*.9
else :
    payble=purchase_amount

print(f'your payable is $ {payble:.2f}')
print(
    
)