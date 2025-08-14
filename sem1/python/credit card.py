expiration_month=int(input('Enter the expiration month (1-12):'))
card_type=input('Enter your card type(Mastercard/Visa):').lower()

if (expiration_month>=1 and expiration_month<=12) and (card_type in ['mastarcard','visa']):
    print('Credit card is Valid')
else:
    print('Credit card is not valid')