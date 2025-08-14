print('Program to calculate your attendence and Display your elegibility for exam\n')
class_held=int(input('Enter the no. of classes held => '))
class_attended=int(input('Enter the no. of classes you have attended => '))
Attendence_percentage=class_attended/class_held*100
print('\nYour Attendence percentage is',Attendence_percentage,'%')
if Attendence_percentage>=75:
    print('\nYou are elegible for Examination!')
else :
    medical=str(input('\nDid you have any medical reasion for your decreased attendence? (yes/no)\n=> '))
    if medical=='yes' or medical=='y':
        print('\nYou are elegible for Examination due to Medical reasions!')
    else :
        print('\nYour are not eligable for Examination due to your low attendence in classes!')
input('\nyou may click enter to exit program~')