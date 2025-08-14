m=int(input('Marks = '))
if m>=0 and m<=100 :
    if m>=90:
        Grade='A'
    elif m>=80:
        Grade='B'
    elif m>=70:
        Grade='C'
    elif m>=60:
        Grade='D'
    else :
        Grade='E'
    print('your Grade is',Grade)
else :
    print('not elegible')