num=int(input())

# print(num,end=' ')
# for  i in range((-num)+1,0):
#     print('*',-i,end=' ')

# fac=num
# for i in range((-num)+1,0):
#     fac*=-i
# print (fac)

def factorial(num):
    fac=num
    for i in range(1,num):
        fac*=i
    return print(fac)

factorial(num)