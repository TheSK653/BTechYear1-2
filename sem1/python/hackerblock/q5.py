# Given a list of numbers, stop processing input after the cumulative sum of all the input becomes negative.


# s=[]
# sum=0
# while True:
#     n=int((input()))
#     if n<=1000 and n>=-1000:
#         sum+=n
#         s.append(n)
#     if sum<0:
#         s.pop(-1)
#         break
# for i in s:
#     print(i)

# ALT

sum=0
while True:
    n=int(input())
    sum+=n
    if sum<0:
        break
    print(n)