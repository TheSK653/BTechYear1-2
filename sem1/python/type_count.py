password=input('Enter password\n=>')
alphabet,digit,space,special_charecter=0,0,0,0
for i in password:
    if i.isalpha():
        alphabet+=1
    elif i.isdigit():
        digit+=1
    elif i.isspace():
        space+=1
    else:
        special_charecter+=1
print(f'alphabet = {alphabet}')
print(f'digit = {digit}')
print(f'space = {space}')
print(f'special charecter = {special_charecter}')

#ALT
# import re
# str='Abc123 @34'
# print('alphabet',int(len(re.findall(r'\w',str))-int(len(re.findall(r'\d',str)))))
# print('digit',len(re.findall(r'\d',str)))
# print('space',len(re.findall(r'\s',str)))
# print('special',int(len(re.findall(r'\W',str))-int(len(re.findall(r'\s',str)))))