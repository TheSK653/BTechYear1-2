age=int(input('Enter your age to get the cost of your Tick for a Theme Park\n=>'))
if age>=4:
    if age>=18:
        price='$20'
    elif age>=13:
        price='$15'
    else:
        price='$10'
    print('Price of your ticket =',price)
elif age>=0:
        print('Free Enter to the Theme Park!')
else:
     print('ERROR')