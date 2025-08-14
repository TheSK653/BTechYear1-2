# Problem Statement: Armstrong Number Manipulation

#     Write a Python script that takes a starting and ending number from the user and identifies Armstrong numbers within that range. 
#     For Armstrong numbers less than 300, print them as they are. 
#     For Armstrong numbers greater than or equal to 300, reverse each number and display both the original and reversed numbers side by side.
    
#     Example:
#         Enter the starting range: 100
#         Enter the ending range: 2000
#         Original and reversed Armstrong numbers within the range 100 to 2000:
#         153
#         370 -> 073
#         371 -> 173
#         407 -> 704
#         1634 -> 4361

#     PERFOMR THE ABOVE BY USING FUNCTION AND LISTS CONCEPT.

def arm(lower,upper):
    for num in range(lower,upper+1):
        ord=len(str(num)) 
        sum=0
        
        temp=num
        while temp>0:
            digit=temp%10
            sum+=digit**ord
            temp//=10

        # for n in str(num):
        #     sum+=int(n)**ord

        if sum==num:
            print(num)   
x=int(input())
y=int(input())
arm(x,y)
