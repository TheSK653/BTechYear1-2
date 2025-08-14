GPA=float(input('Enter your GPA\n=>'))
ans=input('did you participated in extracurriculam activities?(yes/no)\n=>')
if GPA>=3.5 and (ans=='Yes'or ans=='yes' or ans=='Y' or ans=='y'):
    print('you are eligible for scholarship')
else:
    print('you are not eligible for scholarship')