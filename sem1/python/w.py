accessed=str('SOHAM')
n=input('ID proof needed to run the program\nEnter you name :-\n').upper()
if n==accessed:
   print('\nAccess has been granted\nWelcome to the newly created code,\n Mister '+n,':)\n');
   a=input(str('Do you want to calculate your age? (yes/no)\n'))
   if a=='yes' or a=='y':
      c=int(input('\nTo know your age\nEnter current year = '))
      b=int(input('Enter your birth year = '))
      age=c-b
      print('your age is',age)
      if age>=18:
         print('You are eligable to apply for driving licence')
      else :
         print('you are not eligable to apply for driving licence')
   else :
      print('You may add another funtion in this code to use 😊-*')
else:
   print('\nAccess has been denied\nID match not founda by the name',n)
input('\n-----End-----')