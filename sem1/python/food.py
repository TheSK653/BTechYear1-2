a1=input('Are you vegetarian?\n=>').lower()
a2=int(input('How much is your bugget?\n=> $'))
a3=int(input('How much time is in your hand?(min.\n=>'))
if a1=='y' or a1=='yes':
    if a2>=10:
        if a3>=30:
            r='Veg Main course'
        elif a3>=20:
            r='large veg pizza'
        elif a3>=10:
            r='ver burger'
        else:
            r='Bevragers/soft drinks'
    elif a2>=5:
        if a3>=30:
            r='Veg Main course'
        elif a3>=20:
            r='large veg pizza'
        elif a3>=10:
            r='ver burger'
        else:
            r='Bevragers/soft drinks'
    elif a2>=5:
        if a3>=30:
            r='Veg Main course'
        elif a3>=20:
            r='large veg pizza'
        elif a3>=10:
            r='ver burger'
        else:
            r='Bevragers/soft drinks'
    elif a2>=0:
        if a3>=30:
            r='Main course with chicken dishes'
        elif a3>=20:
            r='large double chi pizza'
        elif a3>=10:
            r='ver burger'
        else:
            r='Bevragers/soft drinks'
    else:
        r='non'
else:
    if a2>=10:
        if a3>=30:
            r='Main course with chicken dishes'
        elif a3>=20:
            r='large double chi pizza'
        elif a3>=10:
            r='ver burger'
        else:
            r='Bevragers/soft drinks'
    elif a2>=5:
        if a3>=30:
            r='Main course with chicken dishes'
        elif a3>=20:
            r='large double chi pizza'
        elif a3>=10:
            r='ver burger'
        else:
            r='Bevragers/soft drinks'
    elif a2>=5:
        if a3>=30:
            r='Main course with chicken dishes'
        elif a3>=20:
            r='large double chi pizza'
        elif a3>=10:
            r='ver burger'
        else:
            r='Bevragers/soft drinks'
    elif a2>=0:
        if a3>=30:
            r='Main course with chicken dishes'
        elif a3>=20:
            r='large double chi pizza'
        elif a3>=10:
            r='ver burger'
        else:
            r='Bevragers/soft drinks'
    else:
        r='non'
print('Suggested food :-',r)