while True:
    upp_check,low_check,dig_check,special_check=False,False,False,False
    password=input('Enter the password\n=>')
    if len(password)>=12:
        for i in password:
            if i.isupper():
                upp_check=True
            elif i.islower():
                low_check=True
            elif i.isdigit():
                dig_check=True
            else:
                special_check=True
        if upp_check==True and low_check==True and dig_check==True and special_check==True:
            print('The password is strong')
            break
        else:
            print('The password is not strong Enough\n')
    else:
        print('Password should be of 12 charecter\n')