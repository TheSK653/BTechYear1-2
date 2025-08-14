principal=int(input('Calculation of interest of Home Loan\nEnter the following:-\nPrincipal amount = '))
rate_yearly=float(input('Yearly nterest rate = '))
time_yearly=int(input('Time period in years = '))
rate_monthly=rate_yearly/1200
time_monthly=time_yearly*12
print('EMI =',principal*rate_monthly)
print('total interest to be paid =',(principal*((1+rate_monthly)**time_monthly))-principal)


# P x R x (1+R)^N / [(1+R)^N-1] 
# where- ; P = Principal loan amount ;
# N = Loan tenure in months ;
# R = Monthly interest rate