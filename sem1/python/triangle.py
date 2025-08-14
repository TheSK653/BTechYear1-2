print('enter 3 sides of a triangle')
s1=int(input())
s2=int(input())
s3=int(input())
if s1==s2==s3:
    print('equilaterial')
elif s1==s2 or s2==s3 or s1==s3:
    print('isosceles')
else:
    print('scalene')