user_input=int(input('Enter a number '))
num_of_digits=len(str(user_input))
wanna_be_armstrong=0

# temp=user_input
# while temp>0:
#     digit=temp%10
#     wanna_be_armstrong+=digit**num_of_digits
#     temp//=10

for n in str(user_input):
    wanna_be_armstrong+=int(n)**num_of_digits

if user_input==wanna_be_armstrong:
    print(user_input,'is armstrong')
else:
    print(user_input,'isnt armstrong')