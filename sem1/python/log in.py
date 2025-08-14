username='sohamkundu'
password='thisisit'
entery1=str(input('\tLOG IN\nEnter your username = '))
entery2=str(input('Enter your password = '))
if len(entery1)<5:
    print('Username require atleast 5 charecter')
if len(entery2)<8:
    print('Password require atleast 8 charecter')
if len(entery1)>=5 and len(entery2)>=8:
    print('Username and password is eligable')
    if entery1==username and entery2==password:
        print('\tUserID is loged in')
    else:
        print('\t+UserID not found')
input()