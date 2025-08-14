N=int(input())
if N<=1000:
    for i in range(N):
        car_no=int(input())
        if car_no>=0 and car_no<=1000000000:
            even_sum,odd_sum=0,0
            car_no=str(car_no)
            for d in range(len(car_no)):
                if int(car_no[d])%2==0:
                    even_sum+=int(car_no[d])
                else:
                    odd_sum+=int(car_no[d])
            if even_sum%4==0 or odd_sum%3==0:
                print('Yes')
            else:
                print('No')